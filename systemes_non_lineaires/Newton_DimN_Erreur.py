from autograd import grad
import autograd.numpy as an
import numpy as np

def newton_dim2(f,jac, x, iter=100):

    xk = np.array(x)
    h = np.linalg.solve(jac(xk[0], xk[1]), -np.array(f(xk[0], xk[1])))
    while not np.allclose(xk, xk + h, rtol=1e-5) and iter > 0:
        h = np.linalg.solve(jac(xk[0], xk[1]), -np.array(f(xk[0], xk[1])))
        xk = xk + h
        iter -= 1
    return xk

def F(x,y):
    return [an.exp(x)-y, x**2+y**2-16]

def jac(f):
    f1 = lambda x, y: f(x, y)[0]
    f2 = lambda x, y: f(x, y)[1]
    der = [[grad(f1)], [grad(f2)]]

    return np.array(der)

print(newton_dim2(F,jac(F),[2.8, 2.8]))



