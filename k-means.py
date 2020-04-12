import numpy as np
import csv


def k_means (k):
    #getting all the files
    files = ['animals', 'fruits', 'veggies', 'countries']
    animals = np.array(open_file(files[0]))
    fruits = np.array(open_file(files[1]))
    veggies = np.array(open_file(files[2]))
    countries = np.array(open_file(files[3]))

    #creating random points for centroids
    axis = np.random.rand(k,300)
    centroids = []

    #shifting the list by 1 for more simpler code
    for i in range(len(animals)):
        animals[i] = np.roll(animals[i], -1)

    distance = euclidean_distance(axis[0], animals[0])
    d2 = euclidean_distance(axis[1], animals[0])
    #euclidean_distance(axis[0], animals[0])
    print("distance from first centroid is " +str(distance))
    print("distance from second centroid is " +str(d2))

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

k = 2
k_means(k)
