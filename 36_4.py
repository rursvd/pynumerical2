from numpy import zeros

# Define euler function 
def euler(f,t0,tf,y0,n):
    h = (tf - t0)/n
    t = zeros(n+1)
    y = zeros(n+1)
    t[0] = t0
    y[0] = y0
    for i in range(n):
        y[i+1] = y[i] + h * f(t[i],y[i])
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

# Execute the function and print
t, yel = euler(f,t0,tf,y0,n)

print('%9s %9s' % ('t','y'))
for i in range(n+1):
    print('%9.4f %9.4f' % (t[i],yel[i]))
