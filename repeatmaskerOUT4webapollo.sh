input_out=$1
output_name=$2

cat $1 | tr -s ' ' | sed 's/^ *//g' | tr ' ' '\t' > $1.tab_delimited
python repeatmaskerOUT4webapollo.py $1.tab_delimited > $2
rm $1.tab_delimited
