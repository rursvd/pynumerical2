from numpy import exp,sqrt

def simpson(f,a,b,n):
    h = (b-a)/n
    simp = 0.0
    for i in range(1,n):
        x = a + i*h
        if (i%2 == 1):
            simp = simp + 4.0*f(x)
        else:    
            simp = simp + 2.0*f(x)
    simp = h*(f(a) + simp + f(b))/3.0
    return simp

def f(x):
    return x**2*exp(-x)/sqrt(1.0 + x**2)

a = -1.0
b = 1.0
n = 128
T = simpson(f,a,b,n)
print('T = %8.4f' % T)
