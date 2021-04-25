TARGETS="BELGIUM CANADA DENMARK"
data="gasoline"

for target in $TARGETS
do
    d="$target"_6
    python run_experiment.py parallelization.data_run_id=$d data.target_domain=$target
done
   
#    d="$target"_2
#    CUDA_VISIBLE_DEVICES=0 python run_experiment.py parallelization.data_run_id=$d data.target_domain=$target
#    d="$target"_3
#    CUDA_VISIBLE_DEVICES=0 python run_experiment.py parallelization.data_run_id=$d data.target_domain=$target
#    d="$target"_4
#    CUDA_VISIBLE_DEVICES=0 python run_experiment.py parallelization.data_run_id=$d data.target_domain=$target
#    d="$target"_5
#    CUDA_VISIBLE_DEVICES=0 python run_experiment.py parallelization.data_run_id=$d data.target_domain=$target
#    d="$target"_6
#    CUDA_VISIBLE_DEVICES=0 python run_experiment.py parallelization.data_run_id=$d data.target_domain=$target
#    d="$target"_7
#    CUDA_VISIBLE_DEVICES=0 python run_experiment.py parallelization.data_run_id=$d data.target_domain=$target
#    d="$target"_8
#    CUDA_VISIBLE_DEVICES=0 python run_experiment.py parallelization.data_run_id=$d data.target_domain=$target
#    d="$target"_9
#    CUDA_VISIBLE_DEVICES=0 python run_experiment.py parallelization.data_run_id=$d data.target_domain=$target
#    d="$target"_0
#    CUDA_VISIBLE_DEVICES=0 python run_experiment.py parallelization.data_run_id=$d data.target_domain=$target
#done
