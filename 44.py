%matplotlib inline
from numpy import zeros,exp

def rk2(f,t0,tf,y0,n):
    h = (tf - t0)/n; t = zeros(n+1); y = zeros(n+1)
    t[0] = t0; y[0] = y0
    for i in range(n):
        K0 = h * f(t[i], y[i])
        K1 = h * f(t[i] + 3.0/4.0 * h, y[i] + 3.0/4.0 * K0)
        y[i+1] = y[i] + 1.0/3.0 * (K0 + 2.0 * K1)
        t[i+1] = t[i] + h
    return t,y

def heun(f,t0,tf,y0,n):
    h = (tf - t0)/n; t = zeros(n+1); y = zeros(n+1)
    t[0] = t0; y[0] = y0
    for i in range(n):
        yp = y[i] + h * f(t[i],y[i])
        t[i+1] = t[i] + h
        y[i+1] = y[i] + h/2.0 * (f(t[i],y[i]) + f(t[i+1],yp))
    return t,y

def exact(t): return exp((t - 2.0) * t/2.0)
def f(t,y): return  - y + t * y

t0 = 0; tf = 4.0; y0 = 1.0; n = 10

t, yrk2 = rk2(f,t0,tf,y0,n)
t, yhe = heun(f,t0,tf,y0,n)
ext = exact(t)

print('%7s %7s %8s %9s' % ('t', 'yrk2', 'yhe', 'exact'))
for i in range(n+1):
    print('%8.4f %8.4f %8.4f %8.4f' % (t[i],yrk2[i],yhe[i],ext[i]))

plt.plot(t,yrk2,'o-',label='RK2')
plt.plot(t,yhe,'^-',label='Heun')
plt.plot(t,ext,label='Exact')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()
