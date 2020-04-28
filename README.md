The following is the code for K-Means clustering with :
	1)Euclidean distance
	2)Manhattan distance
	3)Cosine similarity
as the distances. Choosing which distance to use is up to the user. L2 normalization has also been implemented. 

Regeardless of what the user chooses, the program will run with the value of k ranging from 1-10. Following which a graph will be shown as the output.
The graph shows the relation between the number of clusters and the value of precision, recall and f-score.

To choose a particular distance and whether or not l2 normalization should be applied, please follow the commands on screen and enter the appropriate value.

The following are the external libraries used in the code along with their purpose:
	1)Numpy - used for l2 normalization, basic arrays and their operation and for initializing the centroids with random values.
	2)Matplotlib - used for plotting the relationship between the number of clusters and the precision, recall and f-score

Disclaimer - Since the initial points of the centroids are chosen at random,  exact results may vary. The graph generally shows a similar relation between the 
	     number of clusters and precision, recall and f-score. If a cluster is empty, the precision is taken as 1.

