from autograd import grad



def newton_dim1(f, x):
    drv = grad(f)
    iter = 100
    xk = x
    while(xk != xk - f(xk)/drv(xk) or iter > 0):
        xk = xk - f(xk)/drv(xk)
        iter -=1
    if(xk == xk - f(xk)/drv(xk)):
          print("solution trouve :")
          return xk
    else:
        print("Max iter atteint")
        return xk

#test pour tanh(x)*cos(x**2)+x-2

import autograd.numpy as an
def f(x):
    return an.tanh(x)*an.cos(x*x)+x-2



print(newton_dim1(f, 2.0))
