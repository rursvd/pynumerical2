from numpy import zeros

def newton(f,df,x0,n):
    x = zeros(n)
    x[0] = x0
    for k in range(n-1):
        x[k+1] = x[k] - f(x[k])/df(x[k])
    return x

def f(x):
    return -x**2 + 6.0 * x - 5.0

def df(x):
    return -2.0 * x + 6.0

n = 7
x0 = -2.0
xn = newton(f,df,x0,n)
    
# printing output
print("%5s %8s" % ('k','x'))
for k in range(n):
    print("%5d %9.4f" % (k+1,xn[k]))
