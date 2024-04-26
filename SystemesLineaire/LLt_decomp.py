from math import *
import numpy as np
# def estSymPos(A):
# on suppose qu'elle est symetrique et definie positive
def solution_LLt(A,B):
    #decomposition LLt
    n = len(A)
    L = [[0]*n for _ in range(n)]
    L[0][0] = round(sqrt(A[0][0]), 5)
    for i in range(1, n):
        L[i][0] = round(A[i][0]/L[0][0], 5)
    for i in range(1, n):
        s = 0
        for k in range(i):
            
            s += (L[i][k]**2)
        L[i][i] = round(sqrt(A[i][i]-s), 5)
        
        if i != n-1 :
            m=0
            for k in range(i):
                m += L[i+1][k]*L[i][k]
            L[i+1][i]= round((A[i+1][i] - m)/L[i][i], 5)
       
    #Solution Ly = b
    y= np.linalg.solve(np.array(L),np.array(B))
    #solution Ax=y
    x= np.linalg.solve(np.transpose(L), y)
    # print(L)   
    # print(np.transpose(L))
    # print(y)
    # print(x)
    return (x, L)
 
# exemple: x doit etre egale a [1,1,1]
# A=[[6, 15, 55], [15, 55, 225], [55, 225,979]]
# b=[76,295,1259]
# print(solution_LLt(A, b))

