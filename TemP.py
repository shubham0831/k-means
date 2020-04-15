from collections import defaultdict
import numpy as np
import csv

'''
centroids contain the coordinates of the centroids
animals is a dict, with animal name as the key and the coordinates of that
    particular animal as the values
cluster is a dict, which contain the animal name which is also the key in the
    animals dict
'''
class assingement:

    def __init__(self, k):
        '''
        TODO:
            1)Check if the animal key is in the cluster
            2)If animal_key is in the cluster then find out the cluster_key
            3)cluster_key will be the same as the centroids position in the 2d centroid shift_array
            4)take the average of all animals in the clusters
            5)averaging will return 300 points aka the coordinates
            6)set the average as the new val of the cluster by using cluster key
        '''

    def k_means(self, k):

        #It will initialize the config variables
        #k = 2
        #creating random points for centroids
        centroids = np.random.rand(k,300)

        #getting empty clusters
        clusters = get_clusters(k)

        #getting all the files
        files = ['animals', 'fruits', 'veggies', 'countries']
        animals = create_dict(open_file(files[0]))
        fruits = create_dict(open_file(files[1]))
        veggies = create_dict(open_file(files[2]))
        countries = create_dict(open_file(files[3]))
        for key in animals.keys():
            distance = []
            for i in range(len(centroids)):
                distance.append(euclidean_distance(centroids[i], animals[key]))
            cluster_id = distance.index(min(distance))
            clusters[cluster_id].append(key)

        print(clusters)
        print(len(clusters))
        print(len(centroids))



    def find_average(self, cluster, centroid):
        centroids = np.random.rand(2,3)
        clusters = {0:['a','b', 'i'], 1:['c', 'j']}
        ani = {'a':[1,2,3], 'b':[4,5,6], 'c':[2,4,6]}
        fru = {'i' : [10,20,30], "j":[5,8,9]}
        new_points = [[],[]]

        for i in range(len(clusters)):
            for b in range(3):
                sum = 0
                for k in ani.keys():
                    if k in clusters[i]:
                        sum += ani[k][b]
                for k in fru.keys():
                    if k in clusters[i]:
                        sum += fru[k][b]

                sum = sum/len(clusters[i])
                new_points[i].append(sum)

        for i in centroids:
            print(i)

        for i in range(len(centroids)):
            centroids[i] = new_points[i]

        print("after")

        for i in centroids:
            print(i)



    def euclidean_distance(self, centroid, data):
        sum = 0
        for i in range(len(data)):
            sum += abs(float(data[i]) - centroid[i])
        distance = (sum)**0.5
        return distance


    def open_file(self, file_name):
        with open(file_name, 'r') as f:
            file_name = list(csv.reader(f, delimiter = ' '))
        return file_name

    def get_clusters(self, k):
        clusters = {}
        for i in range(k):
            clusters.setdefault(i, [])
        return clusters

    def shift_array(self, arr):
        #helper function to shirt the array by -1 to make code much simpler
        for i in range(len(arr)):
            arr[i] = np.roll(arr[i], -1)
        return arr

    #this function returns a dictionary with the animal name as the key, and the embeddings as the value
    def create_dict(self, animals):
        dict = {}
        for i in range(len(animals)):
            dict.setdefault(animals[i][0], [])

        animals = shift_array(animals)

        for i in range(len(animals)):
            for k in range(len(animals[i]) -1 ):
                dict[animals[i][-1]].append(animals[i][k])

        return dict

x = assingement()
x.k_means(2)
