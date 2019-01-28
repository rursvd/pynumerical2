from numpy import zeros

# Define rk4_set function
def rk4_set(g,f,t0,tf,y0,v0,n):
    h = (tf - t0)/n
    t = zeros(n+1)
    y = zeros(n+1)
    v = zeros(n+1)
    t[0] = t0
    y[0] = y0
    v[0] = v0
    for i in range(n):
        K0 = h * g(t[i],y[i],v[i])
        M0 = h * f(t[i],y[i],v[i])
        K1 = h * g(t[i] + h/2.0, y[i] + K0/2.0, v[i] + M0/2.0)
        M1 = h * f(t[i] + h/2.0, y[i] + K0/2.0, v[i] + M0/2.0)
        K2 = h * g(t[i] + h/2.0, y[i] + K1/2.0, v[i] + M1/2.0)
        M2 = h * f(t[i] + h/2.0, y[i] + K1/2.0, v[i] + M1/2.0)
        K3 = h * g(t[i] + h, y[i] + K2, v[i] + M2)
        M3 = h * f(t[i] + h, y[i] + K2, v[i] + M2)
        y[i+1] = y[i] + 1.0/6.0 * (K0 + 2.0 * K1 + 2.0 * K2 + K3)
        v[i+1] = v[i] + 1.0/6.0 * (M0 + 2.0 * M1 + 2.0 * M2 + M3)
        t[i+1] = t[i] + h
    return t,y,v

# Define functions
def g(t,y,v):
    return 1.0 + v - y**2 - v**2

def f(t,y,v):
    return 1.0 - y - y**2 - v**2

# Set initial conditions
t0 = 0.0
tf = 4.0
y0 = 0.0
v0 = 1.0
n = 5

# Execute RK4_Set   
t, y, v = rk4_set(g,f,t0,tf,y0,v0,n)

# Print results
print('%8s %8s %8s' % ('t','y','v')) 
for i in range(n+1):
    print("%9.4f %9.4f %9.4f" % (t[i],y[i],v[i]))
