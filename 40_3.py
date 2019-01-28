from numpy import zeros

# Define ab2 function 
def ab2(f,t0,tf,y0,n):
    h = (tf - t0)/n
    t = zeros(n+1)
    y = zeros(n+1)
    t[0] = t0
    y[0] = y0
    y[1] = y[0] + h * f(t[0],y[0])
    t[1] = t[0] + h
    for i in range(1,n):        
        y[i+1] = y[i] + (3.0/2.0) * h * f(t[i],y[i])-1.0/2.0 * h * f(t[i-1],y[i-1])
        t[i+1] = t[i] + h
    return t,y

# Define functions
def f(t,y): 
    return  t - y

# Set initial conditions
t0 = 0.0
tf = 1.0
y0 = 1.0
n = 5

# Execute AB2
t, yab2 = ab2(f,t0,tf,y0,n)

# Print results
print("%5s %8s" % ('t','y'))
for i in range(n+1):
    print("%8.4f %8.4f" % (t[i],yab2[i]))
