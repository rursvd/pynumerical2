from numpy import array, dot, zeros, set_printoptions
from numpy.linalg import inv

def newton_nonlinear(f1,f2,x10,x20,n,omega):
    x1 = zeros(n)
    x2 = zeros(n)
    x1[0] = x10
    x2[0] = x20
    for k in range(n-1):
        f = array([f1(x1[k],x2[k]),f2(x1[k],x2[k])])
        dx1, dx2 = - omega * dot(inv(j(x1[k],x2[k])),f)
        x1[k+1] = x1[k] + dx1
        x2[k+1] = x2[k] + dx2
    return x1, x2

def j(x1,x2):
    j11 = 2.0 * x1
    j12 = 2.0 * x2
    j21 = 1.0
    j22 = -1.0
    return array([[j11, j12],[j21, j22]])

def f1(x1,x2):
    return x1**2 + x2**2 - 1.0

def f2(x1,x2):
    return x1 - x2 - 1.0

jj = j(1,1)
print("J = ",jj)
x10 = -3.0
x20 = -3.0
omega = 1.5
n = 7
x1, x2 = newton_nonlinear(f1,f2,x10,x20,n,omega)

set_printoptions(precision=4)
print("x1 = ", x1)
print("x2 = ", x2)

