import numpy as np
import matplotlib.pyplot as plt
import scipy as scp

import json
import os
import sys


def mean_convergence(array):
    array = np.asarray(array)
    meaned = []
    meaned.append(array[0])
    for i in range(1, array.size):
        meaned.append(np.mean(array[:i]))
    return meaned


DATA_VEC_DIR = "./data_vectorial"
# DATA_VEC_DIR = "./data_vectorial_prova"
for results_dir in os.listdir(DATA_VEC_DIR):
    RESULTS_DIR = DATA_VEC_DIR + "/" + results_dir
    for jsons in (os.listdir(RESULTS_DIR)):
        print(jsons)
        with open(RESULTS_DIR + "/" + jsons) as file:
            pointed_file = json.load(file)
            lifeTime = [[], []]
            lifeTimeU1 = [[], []]
            lifeTimeU2 = [[], []]
            queueLengthU1 = [[], []]
            queueLengthU2 = [[], []]
            for repetition_name in pointed_file:
                print("\t" + repetition_name)
                vectors = pointed_file[repetition_name]["vectors"]
                for vector in vectors:
                    if vector['name'] == 'lifeTime:vector' and vector['module'] == 'Pizza.sink':
                        print(vector['name'])
                        lifeTime[0].append(np.asarray(vector['time']))
                        lifeTime[1].append(np.asarray(mean_convergence(vector['value'])))
                    elif vector['name'] == 'lifeTimeU1:vector' and vector['module'] == 'Pizza.sink':
                        print(vector['name'])
                        lifeTimeU1[0].append(np.asarray(vector['time']))
                        lifeTimeU1[1].append(np.asarray(mean_convergence(np.array(vector['value']))))
                    elif vector['name'] == 'lifeTimeU2:vector' and vector['module'] == 'Pizza.sink':
                        print(vector['name'])
                        lifeTimeU2[0].append(np.asarray(vector['time']))
                        lifeTimeU2[1].append(np.asarray(mean_convergence(np.array(vector['value']))))
                    elif vector['name'] == 'queueLength:vector' and vector['module'] == 'Pizza.EntryQueueU1':
                        print(vector['name'])
                        queueLengthU1[0].append(np.asarray(vector['time']))
                        queueLengthU1[1].append(np.asarray(mean_convergence(np.array(vector['value']))))
                    elif vector['name'] == 'queueLength:vector' and vector['module'] == 'Pizza.EntryQueueU2':
                        print(vector['name'])
                        queueLengthU2[0].append(np.asarray(vector['time']))
                        queueLengthU2[1].append(np.asarray(mean_convergence(np.array(vector['value']))))
            # Plotting data from aggragated array
            for measure in lifeTime, lifeTimeU1, lifeTimeU2, queueLengthU1, queueLengthU2:
                measure = np.asarray(measure)
                print(measure.size)
                fig, ltx = plt.subplots()
                for i in range(0, measure.size):
                    ltx.plot(measure[0][i], measure[1][i])
                plt.show()
            print("DONE")
            exit(0)

