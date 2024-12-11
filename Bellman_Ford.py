import numpy as np

def bellman_ford(C):
    # C is the cost mastrix extracted from the graph.
    n = len(C)
    # Copying as to not modify orginal matrix.
    D = np.copy(C)

    # The Bellman-Ford algorithm only computes the shortest distance of all nodes to a single source node.
    # We iterate the algorithm for all possible sources to compute the distance matrix.
    for source in range (0, n):
        
        dist = np.full((n), np.inf)
        dist[source] = 0

        for _ in range(n-1):

            for u in range(n):
                for v in range(n):
                    if C[u][v] == np.inf :
                        pass

                    new_dist = dist[u] + C[u][v]
                    if dist[v] > new_dist :
                        dist[v] = new_dist

        D[source] = dist
    
    return D



        