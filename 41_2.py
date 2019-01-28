from numpy import zeros

# Define abm2 function
def abm2(f,t0,tf,y0,n):
    h = (tf - t0)/n
    t = zeros(n+1)
    y = zeros(n+1)
    t[0] = t0
    y[0] = y0
    y[1] = y[0] + h * f(t[0],y[0])
    t[1] = t[0] + h
    for i in range(1,n):
        yp = y[i] + (3.0/2.0) * h * f(t[i],y[i]) - 0.5 * h * f(t[i-1],y[i-1])
        t[i+1] = t[i] + h
        y[i+1] = y[i] + 0.5 * h * (f(t[i+1],yp) + f(t[i],y[i]))
    return y

# Define functions
def f(t,y): 
    return  t - y

# Set initial conditions
t0 = 0.0
tf = 1.0
y0 = 1.0
n = 5

# Execute ABM2
yabm2 = abm2(f,t0,tf,y0,n)

# Print results
print("%5s %8s" % ('t','y'))
for i in range(n+1):
    print("%9.4f %9.4f" % (t[i],yabm2[i]))

