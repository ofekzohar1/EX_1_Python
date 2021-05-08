import sys

default_iter = 200
min_arguments = 2
irrelevant_difference = 0.00005


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

    def add_vector_to_cluster(self, another_vector):
        self.cluster_vectors.append(another_vector)

    def get_central(self):
        return self.central

    def get_x_of_vector(self, i):
        return self.central[i]

    def get_cluster_vectors(self):
        return self.cluster_vectors

    def set_cluster_vectors(self, new_cluster_vectors):
        self.cluster_vectors = new_cluster_vectors


# retruns a distance between 2 vectors
def distance(vector_1, vector_2):
    distance_between_vectors = 0
    for number in range(len(vector_2)):
        distance_between_vectors += ((vector_1[number] - vector_2[number]) ** 2)
    distance_between_vectors = distance_between_vectors
    return distance_between_vectors


# receives a list of centroids, transforms in the loop to the central_vector
# builds a list of distances from each cluster to a vector
# uses the distance function
# returns the index of the closest centroids
def finding_cluster(list_of_centroids, vector):
    distance_list = []
    distance_between_central_to_vector = 0
    for centro in list_of_centroids:
        distance_between_central_to_vector = distance(centro.get_central(), vector)
        distance_list.append(distance_between_central_to_vector)
    return distance_list.index(min(distance_list))


# checks if new centrals had changed enough to keep iterating
# return a boolean if we need to keep iterating
def did_cluster_centroid_change(list_of_new_centrals, list_of_old_centrals):
    changed = False
    for ii in range(k):
        for jj in range(dimensions):
            if abs(list_of_new_centrals[ii][jj] - list_of_old_centrals[ii][jj]) > irrelevant_difference:
                changed = True
                break
        if changed:
            break
    return changed


# prints new central after adjusting for the relevant structure
def print_centrals(a_central_list):
    for central in a_central_list:
        pointer = 0
        for l in range(len(central)):
            central[l] = "{:.4f}".format(central[l])
        print(central)


# Updates the new centroids and checks if we need to keep iterating
# return TRUE if we need to keep iterating
def update_centroids(a_centroids_list, k, the_new_central_list):
    old_central_list = []
    for j in range(k):
        old_central_list.append(centroids_list[j].get_central())  # will be used for checking 0.0001 change
        a_centroids_list[j].update_new_central()
        the_new_central_list.append(centroids_list[j].central)
        centroids_list[j].set_cluster_vectors([])
    equal = did_cluster_centroid_change(the_new_central_list, old_central_list)
    return equal


if __name__ == '__main__':
    if len(sys.argv) < min_arguments:
        raise Exception(f"Amount of arguments should be more than 1, amount of arguments={len(sys.argv)}")
    if (not sys.argv[1].isnumeric()) or int(sys.argv[1]) < 1:
        raise Exception(f"K input has to be a number and should exceed 0, k={sys.argv[1]}")
    k = int(sys.argv[1])
    max_iter = default_iter
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
    if k > len(list_of_vectors):
        raise Exception(
            f" K can't be bigger than the number of vectors, K={k},number of vectors ={len(list_of_vectors)}")
    centroids_list = []
    new_central_list = []
    dimensions = len(list_of_vectors[0])
    for i in range(k):
        centroids_list.append(Centroids(list_of_vectors[i], []))
    for num_iteration in range(int(max_iter)):
        for vector in list_of_vectors:
            index = finding_cluster(centroids_list, vector)
            centroids_list[index].add_vector_to_cluster(vector)
        keep_iterating = update_centroids(centroids_list, k, new_central_list)
        if not keep_iterating:
            break
    print_centrals(new_central_list)
