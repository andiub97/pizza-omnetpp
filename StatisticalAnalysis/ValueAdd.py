import pandas as pd

for config in "First", "Second", "Third":
    for n in 2, 3, 4, 5:
        path = "./data/"+config+"-n"+str(n)+"/"
        with open(path) as directory:
            for filename in directory:
                print(filename)


