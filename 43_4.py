from numpy import zeros

# Define rk4_set function 
def rk4_set(f,t0,tf,y0,v0,n):
    h = (tf - t0)/n
    t = zeros(n+1)
    y = zeros(n+1)
    v = zeros(n+1)
    t[0] = t0
    y[0] = y0
    v[0] = v0
    for i in range(n):
        M0 = h * f(t[i],y[i],v[i])
        M1 = h * f(t[i] + h/2.0, y[i] + h/2.0 * v[i], v[i] +  M0/2.0)
        M2 = h * f(t[i] + h/2.0, y[i] + h/2.0 * v[i] + h/4.0 * M0, v[i] + M1/2.0)
        t[i+1] = t[i] + h
        M3 = h * f(t[i+1], y[i] + h * v[i] + h/2.0 * M1, v[i] + M2)
        y[i+1] = y[i] + h * v[i] + h/6.0 * (M0 + M1 + M2)
        v[i+1] = v[i] + (M0 + 2.0 * M1 + 2.0 * M2 + M3)/6.0
    return t,y,v

# Define fuctions
def f(t,y,v):
    return (t**2 - 1.0) * y

# Set initial conditions
t0 = 0
tf = 1
y0 = 1.0
v0 = 0.0
n = 10

# Execute RK4_SET   
t, y, v = rk4_set(f,t0,tf,y0,v0,n)

# Print results
print('%5s %8s %8s' % ('t','y','v')) 
for i in range(n+1):
    print("%9.4f %9.4f %9.4f" % (t[i],y[i],v[i]))

