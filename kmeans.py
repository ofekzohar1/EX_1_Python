import sys


class Centroids:
    def __init__(self, central, cluster_vectors):
        self.central = central
        self.cluster_vectors = cluster_vectors

    # reciving a group of vectors that are in a cluster
    # calculating the new central vector?
    def update_new_central(self):
        new_central_vector = []
        for vector in self.cluster_vectors:
            for i in range(len(vector)):
                new_central_vector[i] += vector[i]
        for x in new_central_vector:
            x = x / len(self.cluster_vectors)
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


# receives a list of centroids, transforms in the loop to the central_vector
# builds a list of distances from each cluster to a vector
# returns the index of the closest centroids
def finding_cluster(list_of_centroids, vector):
    distance_list = []
    distance = 0
    for element in list_of_centroids:
        centrals = element.get_central
        for i in range(len(vector)):
            cc = element.get_x_of_vector(i)
            distance += ((cc * cc) - (vector[i] * vector[i]))
        distance_list.append(distance)
        return distance_list.index(min(distance_list))


if __name__ == '__main__':
    if (not sys.argv[1].isnumeric()) or int(sys.argv[1]) < 1:
        raise Exception("k input is wrong")
    k = int(sys.argv[1])
    max_iter = 200
    if len(sys.argv) == 3:
        if (not sys.argv[2].isnumeric()) or int(sys.argv[2]) < 1:
            max_iter = sys.argv[2]
    list_of_vectors = []
    vector_bulid = []

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
    for i in range(k):
        centroids_list.append(Centroids(list_of_vectors[i], [list_of_vectors[i]]))
    list_of_vectors = list_of_vectors[k + 1:]
    # todo keep_itering = True
    for num in range(max_iter):
        for vector in list_of_vectors:
            index = finding_cluster(centroids_list, vector)
            centroids_list[index].add_vector_to_cluster(vector)
        # resting the centroids group
        for j in range(k):
            temp_central = centroids_list[j].get_central()  # will be used for checking 0.0004 change
            centroids_list[j].update_new_central()
            centroids_list[j].set_cluster_vectors([centroids_list[j].get_central()])
        # todo stoping with 0.004
        # if abs(temp_central[]-centroids_list[j][0])
    print(centroids_list)

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
