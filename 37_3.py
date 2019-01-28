from numpy import zeros

# Define RK2 funcion 
def rk2(f,t0,tf,y0,n):
    h = (tf - t0)/n
    t = zeros(n+1)
    y = zeros(n+1)
    t[0] = t0
    y[0] = y0
    for i in range(n):
        K0 = h * f(t[i], y[i])
        K1 = h * f(t[i] + 3.0/4.0 * h, y[i] + 3.0/4.0 * K0)
        y[i+1] = y[i] + 1.0/3.0 * (K0 + 2.0 * K1)
        t[i+1] = t[i] + h
    return t,y

# Define functions 
def f(t,y): 
    return  t-y

# Set initial conditions
t0 = 0
tf = 1.0
y0 = 1.0
n = 5

# Execute RK2
t, yrk2 = rk2(f,t0,tf,y0,n)

# Print results
print('%9s %9s' % ('t', 'y'))
for i in range(n+1):
    print('%8.4f %8.4f' % (t[i],yrk2[i]))
