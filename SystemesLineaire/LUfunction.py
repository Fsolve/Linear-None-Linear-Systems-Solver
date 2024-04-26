import numpy as np


def solutionLU(A, B):
    n = len(A)
    y = np.zeros(n)
    x = np.zeros(n)
    T = np.zeros((n, n))
    T = A
    K = np.zeros((n, n))
    S = []
    for k in range(n - 1):
        M = np.zeros((n, n))
        L = np.zeros((n, n))
        for i in range(n):
            M[i][i] = 1
            L[i][i] = 1
        for i in range(k + 1, n):
            M[i][k] = round((-T[i][k] / T[k][k]), 5)
            L[i][k] = round((T[i][k] / T[k][k]),5)
        S.append(L)
        T = np.dot(np.array(M), np.array(T))
    for i in range(n-2):
        K = np.dot(np.array(S[i]), np.array(S[i+1]))
    # print("La matrice L est :", '\n', K)
    # print("La matrice U est :", '\n', T)

    # y = sol1(K, B)
    y = np.linalg.solve(K, np.array(B))
    # print("la matrice y est:", '\n',y)
    # x = sol2(T, y)
    x = np.linalg.solve(T, y)

    return (x, K, T)

#Sans utiliser linalg de numpy

# def sol1(A, B):
#     n = len(A)
#     y = np.zeros(n)
#     for i in range(n):
#         for j in range(i):
#             y[i] -= A[i][j]*y[j]
#         y[i] = (y[i] + B[i])/A[i][i]
#     return y



# def sol2(A, B):
#     n = len(A)
#     y = np.zeros(n)
#     for i in range(n-1, -1, -1):
#         for j in range(i+1, n):
#             y[i] -= A[i][j]*y[j]
#         y[i] = (y[i] + B[i])/A[i][i]
#     return y

# a = [[1, 2, 3], [2, 3, -1], [3, 4, 5]]
# b= [1,0,0]
# print("La solution est :", '\n', solutionLU(a, b))
