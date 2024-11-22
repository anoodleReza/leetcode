import numpy as np
import networkx as nx
def main(a):
    n = len(a)
    d = 0.85
    e = np.ones(n) / n
    p0 = np.ones(n) / n
    maxIter = 100
    tol = 1e-6
    dangling = np.ones(n) / n


    # check if A is a valid graph for pagerank
    if not a and len(a) == len(a[0]):
        return

    # normalize the matrix
    a_normalized = np.array(a, dtype=float)
    for i in range(len(a_normalized)):
        row_sum = sum(a_normalized[i])
        if row_sum != 0:
            a_normalized[i] = [x / row_sum for x in a_normalized[i]]

    # # normalize p0
    # p0_sum = sum(p0)
    # if p0_sum != 1:
    #     for i in p0:
    #         i /= p0_sum
    #
    # # normalize e
    # e_sum = sum(p0)
    # if e_sum != 1:
    #     for i in e:
    #         i /= e_sum

    # # normalize dangling nodes
    # dangling_sum = sum(dangling)
    # if dangling_sum != 1:
    #     for i in dangling:
    #         i /= dangling_sum

    # get dangling nodes
    for i in range(n):
        if sum(a_normalized[i]) == 0:
            a_normalized[i] = dangling

    # transpose a
    a_transposed = a_normalized.T

    # main loop
    p = p0
    for i in range(maxIter):
        p_last = p.copy()
        p = d * np.dot(a_transposed, p_last) + (1-d) * e

        # check if converged
        if sum(abs(p - p_last)) < n * tol:
            break
    return p

if __name__ == '__main__':
    a = [[0, 0, 0, 0],
         [1, 0, 1, 0],
         [1, 0, 0, 0],
         [1, 1, 1, 0]]
    result = main(a)
    print(result)





