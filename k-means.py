from collections import defaultdict
from numpy.linalg import norm
import matplotlib.pyplot as plt
import numpy as np
import csv

'''
centroids contain the coordinates of the centroids
animals is a dict, with animal name as the key and the coordinates of that
   particular animal as the values
cluster is a dict, which contain the animal name which is also the key in the
   animals dict
'''


def factorial (number):
    fact = 1
    for i in range(number, 0, -1):
        fact = i*fact
    return fact

def total_trues(number):
    trues = factorial(number)/(factorial(2)*(factorial(number-2)))
    return int(trues)

def print_clusters(clusters):
    for k in clusters.keys():
        print(clusters[k])
        print("\n\n\n")


def normalize(features):
    for k in features.keys():
        l2 = norm(features[k])
        for i in range(len(features[k])):
            features[k][i] = float(features[k][i])/l2
    return features

def find_distance(centroid, features, distance):
    if distance == 1:
        return euclidean_distance(centroid, features)
    elif distance == 2:
        return manhattan_distance(centroid, features)
    else :
        return cosine_similarity(centroid, features)

def k_means (k, dist, nor):
    #getting all the files
    files = ['animals', 'fruits', 'veggies', 'countries']
    animals = create_dict(open_file(files[0]))
    fruits = create_dict(open_file(files[1]))
    veggies = create_dict(open_file(files[2]))
    countries = create_dict(open_file(files[3]))
    features = merge_dict(animals, fruits, veggies, countries)
    if nor == 1:
        features = normalize(features)

    num_clusters = k

    #creating random points for centroids
    centroids = np.random.rand(k,300)
    #getting empty clusters
    clusters = set_clusters(k)
    empty_cluster = set_clusters(k)

    epochs = 20


    for epoch in range(epochs):
        #print(epoch)
        for key in features.keys():
            distance = []
            for i in range(len(centroids)):
                distance.append(find_distance(centroids[i], features[key], distance))
                #distance.append(euclidean_distance(centroids[i], features[key]))
                #distance.append(manhattan_distance(centroids[i], features[key]))
                #distance.append(cosine_similarity(centroids[i], features[key]))
            cluster_id = distance.index(min(distance))
            clusters[cluster_id].append(key)
        centroids = find_average(clusters, centroids, features)
        if epoch != epochs-1:
            for k, v in clusters.items():
                clusters[k] = []

    #print_clusters(clusters)

    p,r,f = metric(clusters, animals, fruits, veggies, countries)
    return p,r,f

def metric(clusters, animals, fruits, veggies, countries):
    total_animals = len(animals)
    total_fruits = len(fruits)
    total_veggies = len(veggies)
    total_countries = len(countries)

    precisions = 0
    recalls = 0

    for k, values in clusters.items():
        ani_clusters = fruits_clusters = veggies_cluster = countries_cluster = 0
        for v in values:
            if v in animals:
                #print(1)
                ani_clusters += 1
            elif v in fruits:
                #print(2)
                fruits_clusters += 1
            elif v in veggies:
                #print(3)
                veggies_cluster += 1
            elif v in countries:
                #print(4)
                countries_cluster += 1
        true_positive = max(ani_clusters, fruits_clusters, veggies_cluster, countries_cluster)
        cluster_size = len(clusters[k])

        if true_positive == ani_clusters:
            all_positive = total_animals
        elif true_positive == fruits_clusters:
            all_positive = total_fruits
        elif true_positive == veggies_cluster:
            all_positive = total_veggies
        elif true_positive == countries_cluster:
            all_positive = total_countries

        p = precision(true_positive, cluster_size)
        r = recall(true_positive, all_positive)
        precisions += p
        recalls += r

    precisions = precisions/len(clusters)
    recalls = recalls/len(clusters)
    f_scores = f_score(precisions,recalls)
    return precisions, recalls, f_scores

def precision(true_positive, cluster_size):
    try:
        p = true_positive/cluster_size
    except ZeroDivisionError:
        p = 1
    return p

def recall(true_positive, all_positive):
    r = true_positive/all_positive
    return r

def f_score(p, r):
    #p is precision, r is recall
    f = (2*p*r)/(p+r)
    return f


def merge_dict(a,b,c,d):
    res = {**a, **b, **c, **d}
    return res

def find_average(clusters, centroids, features):
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
        blah = 1

    for i in range(len(centroids)):
        centroids[i] = new_points[i]

    return centroids

def euclidean_distance(centroid, data):
    sum = 0
    for i in range(len(data)):
        sum += abs((float(data[i]) - centroid[i])**2)
    distance = ((sum)**0.5)
    return distance

def manhattan_distance(centroid, data):
    sum = 0
    for i in range(len(data)):
        sum += abs(float(data[i]) - centroid[i])
    distance = sum
    return distance

def cosine_similarity(centroid, data):
    l_sum = 0
    r_sum = 0
    t_sum = 0
    for i in range(len(data)):
        t_product = abs(float(data[i])*centroid[i])
        t_sum += t_product
        l_sum += abs(float(data[i])**2)
        r_sum += abs(centroid[i]**2)

    l_sum = l_sum**0.5
    r_sum = r_sum**0.5
    distance = t_sum/(l_sum*r_sum)
    return distance


def open_file(file_name):
    with open(file_name, 'r') as f:
        file_name = list(csv.reader(f, delimiter = ' '))
    return file_name

def set_clusters(k):
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

def plot_graph(p,r,f,k):
    plt.plot(k, p, label = "precision")
    plt.plot(k, r, label = "recall")
    plt.plot(k, f, label = "f-score")
    plt.ylabel("Precision, Recall and F-score")
    plt.xlabel("K")
    plt.legend()
    plt.show()
    #print('aaaaaa')

#k = 3
#k_means(k)
precisions = []
recalls = []
f_scores = []
ks = []

print("press 1 for euclidian distance")
print("press 2 for manhattan distance")
print("press 3 for cosine similarity")
dist = int(input())
print("press 1 for l2 normalization")
nor = int(input())


for i in range(10):
    k = i+1
    p,r,f = k_means(k, dist, nor)
    ks.append(k)
    precisions.append(p)
    recalls.append(r)
    f_scores.append(f)
plot_graph(precisions, recalls, f_scores, ks)
