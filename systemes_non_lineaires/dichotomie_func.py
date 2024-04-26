import sys

def dichotomie(f, a, b, iter=100):
        eps = sys.float_info.epsilon
        c = (a + b) / 2
        if(abs(c) < eps or iter == 0):
              
              return (a ,b ,c)
        elif(f(a) * f(c) < 0 ):
             return dichotomie(f, a, c, iter =  iter- 1)
        else:
            return dichotomie(f, c, b, iter = iter - 1)


# fonc = input("entrer la fonction ") #!!!!! x**3-x*3+1  fonction test
# a =float(input("entrer a "))        #-2.5
# b =float(input("entrer b "))        #2
# def f(x):
#     return eval(fonc)    #!!!!!!!!! eval ne marche pas avec les fonctions dans math 
# ajouter la fonction de convertion pour module math


# print("Solution c = ",dichotomie(f, a, b))


