

def jacobi(A, B, X):
    iter = 1
    n = len(B)
    Xp = X
    L=[]
    while iter != 200:
        print(iter , ";", Xp)
        Xp1 = [[0] for _ in range(n)]
        for i in range(n):
            s = 0
            for j in range(n):
                s += A[i][j]*Xp[j]
            Xp1[i] = Xp[i] + (B[i] - s)/A[i][i]
        if iter <= 3:
            L.append(list(map(fl4, Xp1)))
        if Xp == Xp1:
            break
        Xp = Xp1
        iter += 1

    return (list(map(fl4, Xp1)), iter, L) 

def fl4(x):
    return round(x,5)


# a = [[10, -1, 0], [-1, 10, -2],[-2, 0, 10]]
# b= [9, 10,7]
# x=[0,0,0]

# jacobi(a, b, x)

