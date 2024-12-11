import numpy as np

def floyd_warshall(C):

    n = len(C)
    # The algorithm initialises with, and computes directly on, the cost matrix. We copy it as to not modify it.
    D = np.copy(C)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                
                # If the distance from i to j through k is shorter, update value.
                value = (D[i][k] + D[k][j])
                if D[i][j] > value :
                    D[i][j] = value
    
    return D