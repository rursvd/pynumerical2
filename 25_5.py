from numpy import array,mean

def linear_fit(x,y):
    n = len(x)
    xsum = sum(x)
    ysum = sum(y)
    xmean = mean(x)
    ymean = mean(y)
    xysum = 0
    x2sum = 0
    for i in range(n):
        xysum = xysum + x[i]*y[i]
        x2sum = x2sum + x[i]*x[i]
    a = (n * xysum - xsum * ysum)/(n * x2sum - xsum**2)
    b = ymean - a * xmean
    return a,b

x = array([0, 1, 2])  
y = array([1, 3, 2])
a,b = linear_fit(x,y)

print("a = %8.4f" % a)
print("b = %8.4f" % b)
print("y = %8.4f x + %8.4f" % (a, b))
