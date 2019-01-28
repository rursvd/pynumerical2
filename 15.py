%matplotlib inline
from numpy import zeros, sign
import matplotlib.pyplot as plt

def f(x):
    return x**x + 2*x - 6    

def bisection(f,a,b,n):
    c = zeros(n)
    for i in range(n):
        c[i] = (a + b)/2.0
        if sign(f(c[i])) == sign(f(a)):
            a = c[i]
        else:
            b = c[i]
    return c

def secant(f,x0,x1,n):
    xs = zeros(n)     
    for k in range(n):
        x2 = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
        x0 = x1
        x1 = x2
        xs[k] = x2
    return xs       

n = 10
x0 = 0.0
x1 = 3.0

xb = bisection(f,x0,x1,n)
xs = secant(f,x0,x1,n)

# printing output
print("%5s %8s %8s" % ('k','bisection','secant'))
for k in range(n):
    print("%5d %9.4f %9.4f" % (k+1,xb[k],xs[k]))

plt.plot(xb,label='Bisection')
plt.plot(xs,'--',label='Secant')
plt.xlabel('Iterations')
plt.ylabel('x')
plt.legend()
plt.show()
