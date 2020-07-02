import numpy as np
from .partial_loo_krr import PartialLOOCVKRR
from .util import Timer

# Type hinting
from typing import Optional
from causal_da.algorithm.ica_augmenter import ICATransferAugmenter


class AugKRR(PartialLOOCVKRR):
    """The kernel ridge regression predictor that can
    be trained on the pseudo-data generated by an augmenter.
    It performs an analytic-form leave-one-out cross-validation (LOOCV) only on the original data
    to select the kernel bandwidth and the regularization coefficient.
    """
    def fit(self,
            x: np.ndarray,
            y: np.ndarray,
            augmenter: ICATransferAugmenter,
            augment_size: Optional[int] = None):
        """Fit the parameters.

        Parameters:
            x: input data of shape ``(n_data, dim)``.
            y: predicted data of shape ``(n_data, 1)``.
            augmenter: a data augmenter.
            augment_size: the augmentation size (passed to ``augmenter``).
        """
        with Timer() as t:
            X_aug, Y_aug = augmenter.augment_to_size(
                x,
                y,
                include_original=False,
                with_latent=False,
                augment_size=augment_size,
                with_acceptance_ratio=False)
        print(f'[Augmentation]: {t.time}')
        return super().fit(x, y, X_aug, Y_aug)
