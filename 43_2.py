from numpy import zeros

# Define euler_set function 
def euler_set(f,t0,tf,y0,v0,n):
    h = (tf - t0)/n
    t = zeros(n+1)
    y = zeros(n+1)
    v = zeros(n+1)
    t[0] = t0
    y[0] = y0
    v[0] = v0
    for i in range(n):
        y[i+1] = y[i] + h*v[i]
        v[i+1] = v[i] + h*f(t[i],y[i],v[i])
        t[i+1] = t[i] + h
    return t,y,v 

# Define functions
def f(t,y,v):
    return (t**2 - 1.0)*y

# Set initial conditions
t0 = 0
tf = 1
y0 = 1.0
v0 = 0.0
n = 10

# Execute EULER_SET 
t, y, v = euler_set(f,t0,tf,y0,v0,n)

# Print results
print('%5s %8s %8s' % ('t','y','v')) 
for i in range(n+1):
    print("%9.4f %9.4f %9.4f" % (t[i],y[i],v[i]))  
