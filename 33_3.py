from numpy import array

def trapezoidal_non(x,y):
    nm = len(x)-1
    trap = 0.0
    for i in range(nm):
        h = x[i+1] - x[i]
        trap = trap + h * (y[i+1] + y[i])/2.0
    return trap

x = array([1,2,4,7,8])
y = array([1,4,16,49,64])
   
T = trapezoidal_non(x,y)
print('T = %8.4f' % T)
