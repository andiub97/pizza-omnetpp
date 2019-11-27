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


def plot_measure(dir_measure):
    DATA_VEC_DIR = "./data_vectorial"
    # DATA_VEC_DIR = "./data_vectorial_prova"
    for results_dir in os.listdir(DATA_VEC_DIR):
        RESULTS_DIR = DATA_VEC_DIR + "/" + results_dir + "/" + dir_measure
        print(RESULTS_DIR)
        for jsons in (os.listdir(RESULTS_DIR)):
            print(jsons)
            with open(RESULTS_DIR + "/" + jsons) as file:
                pointed_file = json.load(file)
                vectors = pointed_file["vectors"]
                fig, graph = plt.subplots()
                for vector in vectors:
                    graph.plot(vector['time'], mean_convergence(vector['value']))

                graph.set_title(
                    pointed_file['attributes']['configname'] + " - " + dir_measure +
                    '\n\nMax Inventoried PS (n): ' + pointed_file['moduleparams'][0]['**.PS.maxInventoriedPS'] + "\n" +
                    '[U1] InterArrival: ' + pointed_file['moduleparams'][1]['**.U1.interArrivalTime'] + "\n" +
                    '     Service Time PS (for pre-calc): ' + pointed_file['moduleparams'][3][
                        '**.PS.serviceTimeForInventoryU1'] + "\n" +
                    '     Service Time PS: ' + pointed_file['moduleparams'][5]['**.PS.serviceTimeDirectU1'] + "\n" +
                    '     Service Time CS: ' + pointed_file['moduleparams'][8]['**.CS.serviceTimeU1'] + "\n" +
                    '[U2] InterArrival: ' + pointed_file['moduleparams'][2]['**.U2.interArrivalTime'] + "\n" +
                    '     Service Time PS (for pre-calc): ' + pointed_file['moduleparams'][4][
                        '**.PS.serviceTimeForInventoryU2'] + "\n" +
                    '     Service Time PS: ' + pointed_file['moduleparams'][6]['**.PS.serviceTimeDirectU2'] + "\n" +
                    '     Service Time CS: ' + pointed_file['moduleparams'][9]['**.CS.serviceTimeU2'] + "\n" +
                    'Pre-calc probability (p): ' + pointed_file['moduleparams'][7]['**.PS.probabilityProducing'] + "\n"
                )
                graph.autoscale_view()
                # plt.suptitle(pointed_file['attributes']['configname'] + " - " + dir_measure, fontsize=14,
                #             fontweight='bold')
                plt.savefig('./charts/charts_vector' + results_dir.replace('data', '').replace('_json', '') +
                            "/" + dir_measure + "/" + jsons.replace('.json', ''), bbox_inches='tight')
                plt.show()


if __name__ == "__main__":
    plot_measure("lifeTime")
    plot_measure("lifeTimeU1")
    plot_measure("lifeTimeU2")
    plot_measure("queueLengthU1")
    plot_measure("queueLengthU2")
