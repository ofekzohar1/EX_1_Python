import math
import sys


class Centroids:
    def __init__(self, central, cluster_vectors):
        self.central = central
        self.cluster_vectors = cluster_vectors
        self.dim = len(central)

    # reciving a group of vectors that are in a cluster
    # calculating the new central vector?
    def update_new_central(self):
        new_central_vector = []
        for n in range(self.dim):
            new_central_vector.append(0)
        for a_vector in self.cluster_vectors:
            for n in range(self.dim):
                new_central_vector[n] += a_vector[n]
        for n in range(self.dim):
            new_central_vector[n] = (new_central_vector[n] / len(self.cluster_vectors))
        self.central = new_central_vector

    def add_vector_to_cluster(self, vector):
        self.cluster_vectors.append(vector)

    def get_central(self):
        return self.central

    def get_x_of_vector(self, i):
        return self.central[i]

    def get_cluster_vectors(self):
        return self.cluster_vectors

    def set_cluster_vectors(self, new_cluster_vectors):
        self.cluster_vectors = new_cluster_vectors


# retruns distance between 2 vectors
def distance(vector_1, vector_2):
    distance_between_vectors = 0
    for number in range(len(vector_2)):
        distance_between_vectors += math.sqrt(abs((vector_1[i] * vector_1[i]) - (vector_2[i] * vector_2[i])))
    return distance_between_vectors


# receives a list of centroids, transforms in the loop to the central_vector
# builds a list of distances from each cluster to a vector
# uses the distance function
# returns the index of the closest centroids
def finding_cluster(list_of_centroids, vector):
    distance_list = []
    central_vector = []
    for jj in range(dimensions):
        central_vector.append(0)
    distance_between_central_to_vector = 0
    for centro in list_of_centroids:
        for numm in range(dimensions):
            central_vector[numm] = centro.get_x_of_vector(numm)
        distance_between_central_to_vector = distance(central_vector, vector)
        distance_list.append(distance_between_central_to_vector)
    return distance_list.index(min(distance_list))


if __name__ == '__main__':
    if (not sys.argv[1].isnumeric()) or int(sys.argv[1]) < 1:
        raise Exception(f"k input has to be a number and should exceed 0, k={sys.argv[1]}")
    k = int(sys.argv[1])
    max_iter = 200
    if len(sys.argv) == 3:
        if (sys.argv[2].isnumeric()) and int(sys.argv[2]) > 1:
            max_iter = sys.argv[2]
        else:
            raise Exception(f"max_iter input has to be a number and should exceed 0, max_iter={sys.argv[2]}")
    list_of_vectors = []
    vector_bulid = []

    # todo exception for input
    while True:
        try:
            for line in input().split('\n'):
                row_str = line.split(",")
                for num in row_str:
                    vector_bulid.append(float(num))
                list_of_vectors.append(vector_bulid)
                vector_bulid = []
        except EOFError:
            break
    # def main(k, max_iter=200, path=""):
    # list_of_vectors = move_data_to_array(path)
    centroids_list = []
    dimensions = len(list_of_vectors[0])
    for i in range(k):
        centroids_list.append(Centroids(list_of_vectors[i], []))
    for num in range(int(max_iter)):
        for vector in list_of_vectors:
            index = finding_cluster(centroids_list, vector)
            centroids_list[index].add_vector_to_cluster(vector)
        old_central_list = []
        new_central_list = []
        # resting the centroids group
        for j in range(k):
            old_central_list.append(centroids_list[j].get_central())  # will be used for checking 0.0004 change
            centroids_list[j].update_new_central()
            new_central_list.append(centroids_list[j].central)
            centroids_list[j].set_cluster_vectors([])
        # todo stoping with 0.004
        count = 0
        for old_central in old_central_list:
            if distance(old_central, new_central_list[old_central_list.index(old_central)]) < 0.005:
                count += 1
        if count == k:
            break
    for central in new_central_list:
        print(central)

    """
    path = "C:\\Users\\ben\\Downloads\\personal\\school\\coding_project\\h.w\\1\\tests\\input_1.txt"
    main(5, 600, path)

def move_data_to_array(file_path):
    my_vectors = open(file_path, "r")
    list_of_vectors = []
    vector_bulid = []
    amount_of_vectors = 0
    for line in my_vectors.readlines():
        row_str = line.split(",")
        for e in row_str:
            vector_bulid.append(float(e))
        list_of_vectors.append(vector_bulid)
        vector_bulid = []
    my_vectors.close()
    return list_of_vectors
    """
