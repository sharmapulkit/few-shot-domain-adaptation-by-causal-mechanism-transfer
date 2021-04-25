from sklearn.metrics import mean_squared_error
from causal_da.components.aug_predictor import AugKRR
from causal_da.api_support.assessment_base import StandardAssessmentBase

# Type hinting
import hydra
import os
from pathlib import Path
from importlib import import_module
from omegaconf import DictConfig, OmegaConf
import hydra
import numpy as np
import torch

from typing import Optional
from causal_da.components.aug_predictor.partial_loo_krr import PartialLOOCVKRR

from causal_da.ICML2020_api import CausalMechanismTransferICML2020API
from causal_da.api_support.logging import MongoAndSacredRunLogger, PandasParamHistoryManager
from causal_da.api_support.evaluator_runner import EvaluatorRunner

from support.database.records_aggregator import MongoAggregator
from support.data import get_or_find_cached_data
from support.evaluate import get_epoch_evaluator_runner, get_augmenter_evaluators
from support.database.mongo import get_mongo_observer, get_table

# Importing this here will enable loading the dataset-wise module on the fly.
import data


@hydra.main(config_path='config/config.yaml')
def main(cfg: DictConfig):
    data_name = cfg.data.name
    data_path = hydra.utils.to_absolute_path(cfg.data.path)
    max_threads = cfg.misc.max_threads
    data_run_id = cfg.parallelization.data_run_id
    cfg.method.augment_size = eval(cfg.method.augment_size)
    cfg.recording.save_model_path = hydra.utils.to_absolute_path(
        cfg.recording.save_model_path)
    cfg.recording.data_cache_base_path = hydra.utils.to_absolute_path(
        cfg.recording.data_cache_base_path)
    data_cache_base_path = cfg.recording.data_cache_base_path

    # mongo_params = cfg.database.mongo_host, cfg.database.mongo_port, cfg.database.mongo_user, cfg.database.mongo_pass, cfg.database.mongo_dbname

    ######
    ## Get data
    ##
    if cfg.data.target_domain is not None:
        data_cache_name = f'{data_name}_{data_run_id}_{cfg.data.target_domain}'
    else:
        data_cache_name = f'{data_name}_{data_run_id}'

    data_module = import_module(f'data.{data_name}')
    dataset = data_module.get_data(cfg.data.path)
    (X_src, Y_src, c_src, X_tar_tr, Y_tar_tr, X_tar_te, Y_tar_te, c_tar_tr,
     c_tar_te), target_c = get_or_find_cached_data(
         dataset,
         data_cache_name,
         data_cache_base_path,
         target=cfg.data.target_domain,
         n_target_c=1,
         path=data_path,
         return_target_c=True)

    metrics: dict = {'MSE': mean_squared_error}
    predictor = PartialLOOCVKRR()
    predictor.fit(X_src, Y_src, None, None, None)
    y_pred = predictor.predict(X_tar_te)

    dicts = {**{
            'AugKRR_' + name: metric(Y_tar_te, y_pred)
            for name, metric in metrics.items()
        },
        **{
            'AugKRR_selected' + name: val
            for name, val in predictor.get_selected_params().items()
        }}

    print("Target Domain:", data_run_id)
    print(dicts)

    return dicts

if __name__=="__main__":
    main()