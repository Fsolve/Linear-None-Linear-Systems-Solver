

def seidel(A, B, X):
    n = len(A)
    Xp = X
    iter = 1
    L=[]
    while iter != 200:
        Xp1 = [0 for i in range(n)]
        for i in range(n):
           d = B[i]
           for j in range(i):
              d -= A[i][j] * Xp1[j]
           for j in range(i, n):
              d -= A[i][j] * Xp[j]
           Xp1[i] = d/A[i][i] + Xp[i]
        # print(Xp1)
        # print(iter)
        
        if iter <= 3:
            L.append(list(map(fl4, Xp1)))
        if Xp == Xp1:
            break
        Xp = Xp1
        iter += 1
    
  
    return (list(map(fl4, Xp1)), iter, L) 

def fl4(x):
    return round(x,5)


# exemple pour test
# a = [[10, -1, 0], [-1, 10, -2],[-2, 0, 10]]
# b= [9, 10,7]
# x=[0,0,0]
    

# l= seidel(a, b, x)
# print(l[0])
# print("iter:",l[1])
# i =1
# for x in l[2]:
#     print("x", i," :",x)
#     i += 1
    
