from numpy import zeros

# Define abm4 funciton
def abm4(f,t0,tf,y0,n):
    h = (tf - t0)/n
    t = zeros(n+1)
    y = zeros(n+1)
    t[0] = t0
    y[0] = y0
    # RK4 
    for i in range(3):
        K0 = h * f(t[i], y[i])
        K1 = h * f(t[i] + h/2.0, y[i] + K0/2.0)
        K2 = h * f(t[i] + h/2.0, y[i] + K1/2.0)
        K3 = h * f(t[i] + h, y[i] + K2)
        y[i+1] = y[i] + 1.0 / 6.0 * (K0 + 2.0 * K1 + 2.0 * K2 + K3)
        t[i+1] = t[i] + h
    
    # Predictor and Corrector    
    for i in range(3,n):
        a0 = f(t[i],y[i])
        a1 = f(t[i-1],y[i-1])
        a2 = f(t[i-2],y[i-2])
        a3 = f(t[i-3],y[i-3])
        yp = y[i] + h / 24.0 * (55.0 * a0 - 59.0 * a1 + 37.0 * a2 - 9.0 * a3)
        t[i+1] = t[i] + h
        b0 = f(t[i+1],yp)
        b1 = f(t[i],y[i])
        b2 = f(t[i-1],y[i-1])
        b3 = f(t[i-2],y[i-2])
        y[i+1] = y[i] + h / 24.0 * (9.0 * b0 + 19.0 * b1 - 5.0 * b2 + b3)
    return t,y

# Define functions
def f(t,y): 
    return  t - y

# Set initial conditions
t0 = 0.0
tf = 1.0
y0 = 1.0
n = 5

# Execute ABM4
t, yabm4 = abm4(f,t0,tf,y0,n)

# Print results
print("%5s %8s" % ('t','y'))
for i in range(n+1):
    print("%9.4f %9.4f" % (t[i],yabm4[i]))
