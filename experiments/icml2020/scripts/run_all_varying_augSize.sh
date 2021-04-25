TARGETS="AUSTRIA BELGIUM JAPAN"
data="gasoline"

for augment_size in "'10'" "'20'" "'40'" "'80'" "'160'" "'320'"
do
    for target in $TARGETS
    do
        d="$target"_1
        python run_experiment.py parallelization.data_run_id=$d$augment_size data.target_domain=$target method.augment_size=$augment_size
        d="$target"_2
        python run_experiment.py parallelization.data_run_id=$d$augment_size data.target_domain=$target method.augment_size=$augment_size
        d="$target"_3
        python run_experiment.py parallelization.data_run_id=$d$augment_size data.target_domain=$target method.augment_size=$augment_size
        d="$target"_4
        python run_experiment.py parallelization.data_run_id=$d$augment_size data.target_domain=$target method.augment_size=$augment_size
        d="$target"_5
        python run_experiment.py parallelization.data_run_id=$d$augment_size data.target_domain=$target method.augment_size=$augment_size
        d="$target"_6
        python run_experiment.py parallelization.data_run_id=$d$augment_size data.target_domain=$target method.augment_size=$augment_size
        d="$target"_7
        python run_experiment.py parallelization.data_run_id=$d$augment_size data.target_domain=$target method.augment_size=$augment_size
        d="$target"_8
        python run_experiment.py parallelization.data_run_id=$d$augment_size data.target_domain=$target method.augment_size=$augment_size
        d="$target"_9
        python run_experiment.py parallelization.data_run_id=$d$augment_size data.target_domain=$target method.augment_size=$augment_size
        d="$target"_0
        python run_experiment.py parallelization.data_run_id=$d$augment_size data.target_domain=$target method.augment_size=$augment_size
    done
done
