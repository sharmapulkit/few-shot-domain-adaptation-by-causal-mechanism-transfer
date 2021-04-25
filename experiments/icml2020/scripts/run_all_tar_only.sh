TARGETS="AUSTRIA BELGIUM CANADA DENMARK FRANCE GERMANY GREECE IRELAND ITALY JAPAN NETHERLA NORWAY SPAIN SWEDEN SWITZERL TURKEY U.K. U.S.A."
data="gasoline"

for target in $TARGETS
do
    d="$target"_1
    python AugKRR_wo.py parallelization.data_run_id=$d data.target_domain=$target
    d="$target"_2
    python AugKRR_wo.py parallelization.data_run_id=$d data.target_domain=$target
    d="$target"_3
    python AugKRR_wo.py parallelization.data_run_id=$d data.target_domain=$target
    d="$target"_4
    python AugKRR_wo.py parallelization.data_run_id=$d data.target_domain=$target
    d="$target"_5
    python AugKRR_wo.py parallelization.data_run_id=$d data.target_domain=$target
    d="$target"_6
    python AugKRR_wo.py parallelization.data_run_id=$d data.target_domain=$target
    d="$target"_7
    python AugKRR_wo.py parallelization.data_run_id=$d data.target_domain=$target
    d="$target"_8
    python AugKRR_wo.py parallelization.data_run_id=$d data.target_domain=$target
    d="$target"_9
    python AugKRR_wo.py parallelization.data_run_id=$d data.target_domain=$target
    d="$target"_0
    python AugKRR_wo.py parallelization.data_run_id=$d data.target_domain=$target
done
