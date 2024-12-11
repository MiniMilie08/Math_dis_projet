import numpy as np
from Dijkstra import dijkstra
from Bellman_Ford import bellman_ford
from Floyd_Warshall import floyd_warshall
import time as t

# Graph .csv file representation.
graph_csv = 'graph14.csv'


def main():

    # - Importing the graph's costs matrix C -

    # Reads the .csv file with string values and creates numpy matrix.
    C_str_matrix = np.genfromtxt(graph_csv, delimiter=',', dtype=str)

    # Replaces 'inf' string with np.inf and converts all values to floats.
    C = np.where(C_str_matrix == 'inf', np.inf, C_str_matrix.astype(float))



    # - Computing distance matrices -

    time_D = None
    time_BF = None
    time_FW = None

    # Calling the different algorithm implentations to compute the respective distance matrices.
    
    
    timer = t.time()
    D_Dijkstra = dijkstra(C)
    time_D = t.time() - timer

    timer = t.time()
    D_Bellman_Ford = bellman_ford(C)
    time_BF = t.time() - timer

    timer = t.time()
    D_Floyd_Warshall = floyd_warshall(C)
    time_FW = t.time() - timer

    # Without computing time.
    #D_Dijkstra =        dijkstra(C)
    #D_Bellman_Ford =    bellman_ford(C)
    #D_Floyd_Warshall =  floyd_warshall(C)


    
    # - Printing results -

    # Cost matrix and the distance matrices computed by their respective algorithms.
    print('\nCost matrix : \n', C, '\n')
    print('\nDijkstra distance matrix \nTime :', time_D,'s\n', D_Dijkstra, '\n')
    print('\nBellman-Ford distance matrix :\nTime :', time_BF,'s\n', D_Bellman_Ford, '\n')
    print('Floyd_Warshall distance matrix :\nTime :', time_FW,'s\n', D_Floyd_Warshall)

    # Prints if results match.
    print('\nAll D matrices match: ', ((D_Dijkstra == D_Bellman_Ford).all() == (D_Dijkstra == D_Floyd_Warshall).all()))



# Defining the main running function
if __name__ == '__main__':
    main()