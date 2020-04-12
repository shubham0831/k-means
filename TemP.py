import collections
import csv
import numpy as np
from collections import defaultdict

def create_dict(animals):
    dict = {}
    print(type(dict))
    for i in range(len(animals)):
        dict.setdefault(animals[i][0], [])

    animals = shift_array(animals)

    for i in range(len(animals)):
        for k in range(len(animals[i]) -1 ):
            dict[animals[i][-1]].append(animals[i][k])

    for v in dict.values():
        print(len(v))


    return dict

def open_file(file_name):
    with open(file_name, 'r') as f:
        file_name = list(csv.reader(f, delimiter = ' '))
    return file_name

def shift_array(arr):
    #helper function to shirt the array by -1 to make code much simpler
    for i in range(len(arr)):
        arr[i] = np.roll(arr[i], -1)
    return arr


animals = create_dict(open_file('animals'))
#create_dict(animals)
