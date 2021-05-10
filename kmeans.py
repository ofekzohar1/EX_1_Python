import sys
default_iter = 200
min_arguments = 2
irrele_diff = 0.00005


class Cluster:
    def __init__(self, central):
        self.prev_central = []
        self.curr_central = central
        self.counter = 0
        for n in range(len(central)):
            self.prev_central.append(0)

    def init_curr_central(self):
        for i in range(len(self.curr_central)):
            self.prev_central[i] = self.curr_central[i]
            self.curr_central[i] = 0


# returns a distance between 2 vectors
def distance(vector_1, vector_2):
    distance_between_vectors = 0
    for i in range(len(vector_1)):
        distance_between_vectors += ((vector_1[i] - vector_2[i]) ** 2)
    return distance_between_vectors


# receives a list of centroids, transforms in the loop to the central_vector
# builds a list of distances from each cluster to a vector
# uses the distance function
# returns the index of the closest centroids
def finding_cluster(list_of_clusters, vector):
    distance_list = []
    for cluster in list_of_clusters:
        distance_between_central_to_vector = distance(cluster.prev_central, vector)
        distance_list.append(distance_between_central_to_vector)
    return distance_list.index(min(distance_list))


# reads txt file and converts it to a list of vectors
# returns a list of vectors
def build_list_of_vectors(k):
    vector_build = []
    list_of_vectors = []
    while True:
        try:
            for line in input().split('\n'):
                row_str = line.split(",")
                for num in row_str:
                    vector_build.append(float(num))
                vector_build.append(0)
                list_of_vectors.append(vector_build)
                vector_build = []
        except EOFError:
            break
    amount_of_vectors = len(list_of_vectors)
    if k > amount_of_vectors:
        raise Exception(f" K can't be bigger than the number of vectors, K={k},number of vectors ={amount_of_vectors}")
    return list_of_vectors


# void - initialize clusters from the list of vectors
# param - clusters, all vectors, amount of clusters, dimensions
def create_centrals_for_clusters(list_of_clusters, list_of_vectors, k, dimensions):
    for i in range(k):
        new_vector = []
        vector = list_of_vectors[i]
        for j in range(dimensions):
           new_vector.append(vector[j])
        list_of_clusters.append(Cluster(new_vector))


# initialize clusters after each iteration
# using Cluster class init curr central method
def init_curr_centroid_and_counter(list_of_clusters):
    for cluster in list_of_clusters:
        cluster.init_curr_central()
        cluster.counter = 0


# uses and extra dimension in the vectors to assign which cluster they are in
# creates for the cluster a new curr central that later on will be adjusted by his amount of vectors
def assign_vectors_to_clusters(list_of_vectors, list_of_clusters, dimensions):
    for vector in list_of_vectors:
        my_cluster = finding_cluster(list_of_clusters, vector)
        vector[dimensions] = my_cluster
        list_of_clusters[my_cluster].counter += 1
        for i in range(dimensions):
            list_of_clusters[my_cluster].curr_central[i] += vector[i]


# calculates the new central after knowing the amount of new vectors in his cluster
# returns a value that shows if the vector is changed more thr the relevant difference
def recalc_centroids(list_of_clusters, dimensions):
    changes = 0
    for cluster in list_of_clusters:
        for i in range(dimensions):
            cluster.curr_central[i] /= cluster.counter
            if abs(cluster.prev_central[i] - cluster.curr_central[i]) > irrele_diff:
                changes += 1
    return changes


# prints new central after adjusting for the relevant structure
def print_centrals(list_of_clusters):
    for cluster in list_of_clusters:
        for i in range(len(cluster.curr_central)):
            cluster.curr_central[i] = "{:.4f}".format(cluster.curr_central[i])
        print(*cluster.curr_central, sep=",")


def main():
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
    list_of_vectors = build_list_of_vectors(k)
    list_of_clusters = []
    dimensions = len(list_of_vectors[0]) - 1 # vectors have extra dimension to hold their cluster allocation
    create_centrals_for_clusters(list_of_clusters, list_of_vectors, k, dimensions)
    for num_iteration in range(int(max_iter)):
        init_curr_centroid_and_counter(list_of_clusters)
        assign_vectors_to_clusters(list_of_vectors, list_of_clusters, dimensions)
        keep_iteration = recalc_centroids(list_of_clusters, dimensions)
        if keep_iteration < 1:
            break
    print_centrals(list_of_clusters)


if __name__ == '__main__':
    main()
