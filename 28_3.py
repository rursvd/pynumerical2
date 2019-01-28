from numpy import array,zeros

def coeffs(x0,x1,f0,f1):
    a1= (f1-f0)/(x1-x0)
    a0 = f0 
    return a0, a1

def linear_intp(x,y):
    n = len(x)
    for i in range(n-1):
        x0 = x[i]
        x1 = x[i+1]
        f0 = y[i]
        f1 = y[i+1]
        a0, a1 = coeffs(x0,x1,f0,f1)   
        print("f(x) = %8.4f + %8.4f (x - %8.4f)" % (a0, a1, x0))

x = array([0, 1, 2])
y = array([1, 3, 2])
linear_intp(x,y)
