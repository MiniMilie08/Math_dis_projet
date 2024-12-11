import numpy as np

def bellman_ford(C):
    # C is the cost mastrix extracted from the graph.
    n = len(C)
    # Copying as to not modify orginal matrix.
    D = np.copy(C)

    # The Bellman-Ford algorithm only computes the shortest distance of all nodes to a single source node.
    # We iterate the algorithm for all possible sources to compute the distance matrix.
    for source in range (n):
        
        dist = np.full((n), np.inf)
        dist[source] = 0

        # Relaxing all edges n-1 times.
        for _ in range(n-1):

            for u in range(n):
                for v in range(n):
                    # Skips if path does not exist.
                    if C[u][v] == np.inf :
                        pass

                    # Updating to new shortest distance if found.
                    new_dist = dist[u] + C[u][v]
                    if dist[v] > new_dist :
                        dist[v] = new_dist

        # Appending the distance from source to as the according line in returned matrix.
        D[source] = dist
    
    return D



        