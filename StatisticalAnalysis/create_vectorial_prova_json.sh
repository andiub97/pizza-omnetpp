for results in  "results_prova"
do
cd ../${results}
  for config in "First" "Second" "Third"
  do
    for n in 2 3 4 5
    do
      echo ${config}-n${n}
      scavetool x -f 'module("Pizza.sink") AND (name("lifeTime:vector"))' -o ../StatisticalAnalysis/data_vectorial_prova/data_${results}_json/lifeTime/${config}-n${n}.json -F JSON ${config}-n${n}-*.vec
      scavetool x -f 'module("Pizza.sink") AND (name("lifeTimeU1:vector"))' -o ../StatisticalAnalysis/data_vectorial_prova/data_${results}_json/lifeTimeU1/${config}-n${n}.json -F JSON ${config}-n${n}-*.vec
      scavetool x -f 'module("Pizza.sink") AND (name("lifeTimeU2:vector"))' -o ../StatisticalAnalysis/data_vectorial_prova/data_${results}_json/lifeTimeU2/${config}-n${n}.json -F JSON ${config}-n${n}-*.vec
      scavetool x -f 'module("Pizza.EntryQueueU1") AND (name("queueLength:vector"))' -o ../StatisticalAnalysis/data_vectorial_prova/data_${results}_json/queueLengthU1/${config}-n${n}.json -F JSON ${config}-n${n}-*.vec
      scavetool x -f 'module("Pizza.EntryQueueU2") AND (name("queueLength:vector"))' -o ../StatisticalAnalysis/data_vectorial_prova/data_${results}_json/queueLengthU2/${config}-n${n}.json -F JSON ${config}-n${n}-*.vec
    done
  done
done