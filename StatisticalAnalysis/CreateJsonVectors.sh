cd ../results_no_transient || exit
for config in "First" "Second" "Third"
do
  for n in 2 3 4 5
  do
    echo ${config}-n${n}
    scavetool x -f 'module("*")' -o ../StatisticalAnalysis/data_no_transient_json/${config}-n${n}.json -F JSON ${config}-n${n}-*.vec
  done
done