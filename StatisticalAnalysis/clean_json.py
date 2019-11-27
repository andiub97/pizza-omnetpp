import json
import os

DATA_VEC_DIR = "./data_vectorial"
# DATA_VEC_DIR = "./data_vectorial_prova"
for results_dir in os.listdir(DATA_VEC_DIR):
    RESULTS_DIR = DATA_VEC_DIR + "/" + results_dir
    print("Cleaning " + RESULTS_DIR)
    for measure_dir in os.listdir(RESULTS_DIR):
            MEASURE_DIR = RESULTS_DIR + "/" + measure_dir
            print("\t|")
            print("\t|_ Cleaning " + MEASURE_DIR)
            try:
                for file_json in (os.listdir(MEASURE_DIR)):
                    print("\t\t|")
                    print("\t\t| " + file_json)
                    new_file = {}
                    with open(MEASURE_DIR + "/" + file_json, 'r') as file:
                        pointed_file = json.load(file)
                        for rep in pointed_file:
                            new_file = pointed_file[rep]
                            del pointed_file
                            break
                    with open(MEASURE_DIR + "/" + file_json, 'w') as file:
                        json.dump(new_file, file, indent=4)
                        del new_file
                        print("\t\t|_ " + file_json + ": Cleaned!")
            except:
                print("DIO CANE")

