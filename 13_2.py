
from numpy import zeros

def secant(f,x0,x1,n): 
    xs = zeros(n)
    for k in range(n):
        x2 = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
        x0 = x1
        x1 = x2
        xs[k] = x2
    return xs 

def f(x):
   return -x**2 + 6.0*x -5.0

x0 = -2.0
x1 = 3.0
n = 7
xs = secant(f,x0,x1,n)

print("%5s %8s" % ('k','x'))
for k in range(n):
    print("%5d %9.4f" % (k+1,xs[k]))
