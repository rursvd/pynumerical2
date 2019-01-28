from numpy import zeros

# Define RK4 function
def rk4(f,t0,tf,y0,n):
    h = (tf - t0)/n
    t = zeros(n+1)
    y = zeros(n+1)
    t[0] = t0
    y[0] = y0
    for i in range(n):
        K0 = h * f(t[i], y[i])
        K1 = h * f(t[i] + h/2.0, y[i] + K0/2.0)
        K2 = h * f(t[i] + h/2.0, y[i] + K1/2.0)
        K3 = h * f(t[i] + h, y[i] + K2)
        y[i+1] = y[i] + 1.0/6.0 * (K0 + 2.0 * K1 + 2.0 * K2 + K3)
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

# Execute RK4
t, yrk4 = rk4(f,t0,tf,y0,n)

# Print results
print('%9s %9s' % ('t', 'y'))
for i in range(n+1):
    print('%8.4f %8.4f' % (t[i],yrk4[i]))
