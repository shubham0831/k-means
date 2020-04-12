from collections import defaultdict
import numpy as np
import csv

def k_means (k):
    #getting all the files
    files = ['animals', 'fruits', 'veggies', 'countries']
    animals = create_dict(open_file(files[0]))
    fruits = create_dict(open_file(files[1]))
    veggies = create_dict(open_file(files[2]))
    countries = create_dict(open_file(files[3]))

    #creating random points for centroids
    centroids = np.random.rand(k,300)
    #getting empty clusters
    clusters = get_clusters(k)

    for key in animals.keys():
        distance = []
        for i in range(len(centroids)):
            distance.append(euclidean_distance(centroids[i], animals[key]))
        cluster_id = distance.index(min(distance))
        clusters[cluster_id].append(key)

    print(len(clusters))
    print(len(centroids))

def find_average():
    print(11111)


def euclidean_distance(centroid, data):
    sum = 0
    for i in range(len(data) - 1):
        sum += abs(float(data[i]) - centroid[i])
    distance = (sum)**0.5
    return distance


def open_file(file_name):
    with open(file_name, 'r') as f:
        file_name = list(csv.reader(f, delimiter = ' '))
    return file_name

def get_clusters(k):
    clusters = {}
    for i in range(k):
        clusters.setdefault(i, [])
    return clusters

def shift_array(arr):
    #helper function to shirt the array by -1 to make code much simpler
    for i in range(len(arr)):
        arr[i] = np.roll(arr[i], -1)
    return arr

#this function returns a dictionary with the animal name as the key, and the embeddings as the value
def create_dict(animals):
    dict = {}
    for i in range(len(animals)):
        dict.setdefault(animals[i][0], [])

    animals = shift_array(animals)

    for i in range(len(animals)):
        for k in range(len(animals[i]) -1 ):
            dict[animals[i][-1]].append(animals[i][k])

    return dict

k = 2
k_means(k)

'''
d = distance.index(min(distance))

append values to the dict code:
        clusters[d].append(animals[i])
    where d is the key of the dictionary aka the cluster number
          i is the animal whose euclidean_distance we just calculated

'''

'''
for i in range(len(animals)):
    distance = []
    for k in range(len(axis)):
        distance.append(euclidean_distance(axis[k], animals[i]))
    #print("printing distance for " +str(animals[i][-1]))
    #print("minimum distance for " +str(animals[i][-1]) + " is " +str(min(distance)))
    cluster_id = distance.index(min(distance))
    #print("that means the cluster which " +str(animals[i][-1]) + " will go to is " + str(cluster_id))
    clusters[cluster_id].append(animals[i][-1])
'''
