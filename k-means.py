from collections import defaultdict
import numpy as np
import logging
import csv

'''
centroids contain the coordinates of the centroids
animals is a dict, with animal name as the key and the coordinates of that
    particular animal as the values
cluster is a dict, which contain the animal name which is also the key in the
    animals dict
'''
'''
for epoch in range(epochs):
    for key in features.keys():
        distance = []
        for i in range(len(centroids)):
            distance.append(euclidean_distance(centroids[i], features[key]))
            cluster_id = distance.index(min(distance))
            clusters[cluster_id].append(key)
    centroids = find_average(clusters, centroids, features)
    clusters = set_clusters(k)
    print("after " +str(epoch) + " iter")
    for k in clusters.values():
        print(k)
        print("---------")
    print("--------------------------------------------------------")



for i in range(len(clusters)):
    print("len of " +str(i) +" cluster is " +str(len(clusters[i])))
    if len(clusters[i]) == 0:
        break
    else:
        for b in range(len(clusters[i])):
            sum = 0
            for k in features.keys():
                if k in clusters[i]:
                    sum += float(features[k][b])
            sum = sum/len(clusters[i])
            new_points[i].append(sum)
'''

'''
    for key, values in animals.items():
        distance = []
        for i in range(len(centroids)):
            distance.append(euclidean_distance(centroids[i], values))
        cluster_id = distance.index(min(distance))
        clusters[cluster_id].append(key)
        print(clusters)
        print("-------------")
'''

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('start of program')
def k_means (k):
    logging.debug("in k-means")
    #getting all the files
    files = ['animals', 'fruits', 'veggies', 'countries']
    animals = create_dict(open_file(files[0]))
    fruits = create_dict(open_file(files[1]))
    veggies = create_dict(open_file(files[2]))
    countries = create_dict(open_file(files[3]))
    features = merge_dict(animals, fruits, veggies,countries)

    num_clusters = k

    #creating random points for centroids
    centroids = np.random.rand(k,300)
    #getting empty clusters
    clusters = set_clusters(k)
    empty_cluster = set_clusters(k)

    epochs = 30


    for epoch in range(epochs):
        print(epoch)
        for key in features.keys():
            distance = []
            for i in range(len(centroids)):
                distance.append(euclidean_distance(centroids[i], features[key]))
            cluster_id = distance.index(min(distance))
            clusters[cluster_id].append(key)
        #prob in below line, code never goes into find_average
        centroids = find_average(clusters, centroids, features)
        if epoch != epochs-1:
            for k, v in clusters.items():
                clusters[k] = []
        else:
            for keys in clusters.keys():
                print(clusters[keys])
                print("\n\n\n\n\n\n")



def merge_dict(a,b,c,d):
    res = {**a, **b, **c, **d}
    return res

def find_average(clusters, centroids, features):
#    logging.debug("in avg")
    new_points = []
    try:
        for i in range(len(clusters)):
            sum = np.zeros([300])
            for k,v in features.items():
                if k in clusters[i]:
                    feature_vector = np.array(features[k], dtype = 'float')
                    sum += feature_vector
            sum = sum/len(clusters[i])
            new_points.append(sum)
    except :
        opopopopo = 1

    for i in range(len(centroids)):
        centroids[i] = new_points[i]

#    logging.debug("avg ended")

    return centroids

def euclidean_distance(centroid, data):
#    logging.debug("in eucl distance")
    sum = 0
    for i in range(len(data)):
        sum += abs(float(data[i]) - centroid[i])
    distance = (sum)**0.5
#    logging.debug("euc distance ended")
    return distance


def open_file(file_name):
    with open(file_name, 'r') as f:
        file_name = list(csv.reader(f, delimiter = ' '))
    return file_name

def set_clusters(k):
#    logging.debug("set_cluster")
    clusters = {}
    for i in range(k):
        clusters.setdefault(i, [])
#    logging.debug("set_cluster ended")
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

epochs = 20
k = 6
k_means(k)

clusters = {0:['a','b'], 1:['c']}
centroids = np.random.rand(2,3)
features = {'a':[1,2,3], 'b':[4,6,7], 'c':[10,11,12]}
#find_average(clusters, centroids, features)
