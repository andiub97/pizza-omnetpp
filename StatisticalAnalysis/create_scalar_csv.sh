for data in "results" "results_no_transient"
do
  cd ../${data}
  for config in "First" "Second" "Third"
  do
    for n in 2 3 4 5
    do
      scavetool x -f 'module("*.EntryQueueU1") AND (name("queueLength:mean"))' -o ../StatisticalAnalysis/data/data_${data}/${config}-n${n}/EntryQueueLengthMeanU1.csv -F CSV-S ${config}-n${n}-*.sca
      scavetool x -f 'module("*.EntryQueueU2") AND (name("queueLength:mean"))' -o ../StatisticalAnalysis/data/data_${data}/${config}-n${n}/EntryQueueLengthMeanU2.csv -F CSV-S ${config}-n${n}-*.sca
      scavetool x -f 'module("*.sink") AND (name("lifeTime:mean"))' -o ../StatisticalAnalysis/data/data_${data}/${config}-n${n}/LifeTimeMeanTotal.csv -F CSV-S ${config}-n${n}-*.sca
      scavetool x -f 'module("*.sink") AND (name("lifeTimeU1:mean"))' -o ../StatisticalAnalysis/data/data_${data}/${config}-n${n}/LifeTimeMeanU1.csv -F CSV-S ${config}-n${n}-*.sca
      scavetool x -f 'module("*.sink") AND (name("lifeTimeU2:mean"))' -o ../StatisticalAnalysis/data/data_${data}/${config}-n${n}/LifeTimeMeanU2.csv -F CSV-S ${config}-n${n}-*.sca
      scavetool x -f 'module("*.sink") AND (name("lifeTime:min"))' -o ../StatisticalAnalysis/data/data_${data}/${config}-n${n}/LifeTimeMinTotal.csv -F CSV-S ${config}-n${n}-*.sca
      scavetool x -f 'module("*.sink") AND (name("lifeTimeU1:min"))' -o ../StatisticalAnalysis/data/data_${data}/${config}-n${n}/LifeTimeMinU1.csv -F CSV-S ${config}-n${n}-*.sca
      scavetool x -f 'module("*.sink") AND (name("lifeTimeU2:min"))' -o ../StatisticalAnalysis/data/data_${data}/${config}-n${n}/LifeTimeMinU2.csv -F CSV-S ${config}-n${n}-*.sca
      scavetool x -f 'module("*.sink") AND (name("lifeTime:max"))' -o ../StatisticalAnalysis/data/data_${data}/${config}-n${n}/LifeTimeMaxTotal.csv -F CSV-S ${config}-n${n}-*.sca
      scavetool x -f 'module("*.sink") AND (name("lifeTimeU1:max"))' -o ../StatisticalAnalysis/data/data_${data}/${config}-n${n}/LifeTimeMaxU1.csv -F CSV-S ${config}-n${n}-*.sca
      scavetool x -f 'module("*.sink") AND (name("lifeTimeU2:max"))' -o ../StatisticalAnalysis/data/data_${data}/${config}-n${n}/LifeTimeMaxU2.csv -F CSV-S ${config}-n${n}-*.sca
    done
  done
done