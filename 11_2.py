from numpy import zeros, exp

def newton_rex(f,df,x0,n,omega):
    x = zeros(n)
    x[0] = x0
    for k in range(n-1):
        x[k+1] = x[k] - omega * f(x[k])/df(x[k])
    return x
def f(x):
    return 1.0 - x * exp(1 - x)

def df(x):
    return  x * exp(1 - x) - exp(1 - x)

n = 7
x0 = 0.0
omega = 1.75
xr = newton_rex(f,df,x0,n,omega)
    
print("%5s %8s" % ('k','x'))
for k in range(n):
    print("%5d %9.4f" % (k+1,xr[k]))

