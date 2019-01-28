from numpy import zeros

def heun(f,t0,tf,y0,n):
    h = (tf - t0)/n
    t = zeros(n+1)
    y = zeros(n+1)
    t[0] = t0
    y[0] = y0
    for i in range(n):
        yp = y[i] + h * f(t[i],y[i])
        t[i+1] = t[i] + h
        y[i+1] = y[i] + h/2.0 * (f(t[i],y[i]) + f(t[i+1],yp))
    return t,y  

# Define functions
def f(t,y): 
    return  t - y

# Set initial conditions
t0 = 0.0
tf = 1.0
y0 = 1.0
n = 5

# Execute HEUN
t, yhe = heun(f,t0,tf,y0,n)

# Print results
print('%7s %7s' % ('t','y'))
for i in range(n+1):
    print('%9.4f %9.4f' % (t[i],yhe[i]))
