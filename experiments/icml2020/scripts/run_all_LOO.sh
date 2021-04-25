TARGETS="AUSTRIA BELGIUM CANADA DENMARK FRANCE GERMANY GREECE IRELAND ITALY JAPAN NETHERLA NORWAY SPAIN SWEDEN SWITZERL TURKEY U.K. U.S.A."
data="gasoline"

for target in $TARGETS
do
    d="$target"
    python AugKRR_LOO.py parallelization.data_run_id=$d data.target_domain=$target
done
