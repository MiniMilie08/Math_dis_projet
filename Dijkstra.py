import numpy as np

def dijkstra(C):
    # C is the cost mastrix extracted from the graph.
    n = len(C)
    # Copying as to not modify orginal matrix.
    D = np.copy(C)

    # Dijkstra's algorithm only computes the shortest distance of all nodes to a single source node.
    # We iterate the algorithm for all possible sources to compute the distance matrix.
    for source in range (n):
        
        # Initial distances are given by the cost matrix's copy at the source line.
        # We compute and update distances directly in the matrix D.
        dist = D[source]

        queue = [_ for _ in range(n)]
        # Removing source node from queue.
        queue.remove(source)


        while len(queue) > 0:
            
            # Finding closest neighbour node in queue.
            min_dist = np.inf
            for node in queue:
                if dist[node] <= min_dist :
                    min_dist = dist[node]
                    closest = node
            queue.remove(closest)

            # Updating distances by evaluating from the closest node in queue.
            for node in queue:
                # Comparing old path distance to new path distance.
                new_dist = (C[closest][node] + dist[closest])
                if dist[node] > new_dist:
                    dist[node] = new_dist

    return D