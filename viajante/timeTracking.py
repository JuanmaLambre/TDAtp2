import time
import sys; sys.path.insert(0, '..')
import held_karp

files = [ "15_cities_input.csv", "17_cities_input.csv", "19_cities_input.csv",
         "20_cities_input.csv",
         "21_cities_input.csv", "22_cities_input.csv"]


def get_elapsed_time(dists):
    print("Distance matrix size: ")
    print(str(len(dists)) + " x " + str(len(dists)))
    start = time.time()
    held_karp.held_karp(dists)
    tiempo_total = time.time() - start
    return tiempo_total

if __name__ == '__main__':
    for file in files:
        dists = held_karp.read_distances(file)
        elapsed_time = get_elapsed_time(dists)
        print("Elapsed time:")
        print(elapsed_time)
