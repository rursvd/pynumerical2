from numpy import exp,sqrt

def trapezoidal(f,a,b,n):
    h = (b-a)/n
    trap = 0.0
    for i in range(1,n):
        x = a + i*h
        trap = trap + 2.0 * f(x) 
    trap = h * (f(a) + trap + f(b)) / 2.0
    return trap

def f(x):
    return x**2 * exp(-x)/sqrt(1.0 + x**2)

a = -1.0
b = 1.0
n = 512
T = trapezoidal(f,a,b,n)
print('T = %8.4f' % T)     
