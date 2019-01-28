from numpy import array,mean,log,exp

def nonlinear_fit(x,yo):
    n = len(x)
    y = log(yo)
    xsum = sum(x)
    ysum = sum(y)
    xmean = mean(x)
    ymean = mean(y)
    xysum = sum(x * y)
    x2sum = sum(x**2)
    A = (n * xysum - xsum * ysum)/(n * x2sum - xsum**2)
    B = ymean - A * xmean
    print('A = %8.4f B = %8.4f' % (A, B))
    b = exp(B)
    a = A
    return a,b

def f(a,b,x):
    return b * exp(a * x)

x = array([0, 1, 2, 4])  
yo = array([2, 4, 8, 15])
a,b = nonlinear_fit(x,yo)

print('a = %8.4f b = %8.4f' % (a,b))
print("y = %8.4f exp(%8.4f x)" % (b,a))
