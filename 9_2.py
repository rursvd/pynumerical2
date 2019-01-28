from numpy import zeros

def fixedpoint(g,x0,n):
    x = zeros(n)
    errs = zeros(n)
    x[0] = x0
    for i in range(n-1):
        x[i+1] = g(x[i])
    return x

# Define functions
def g(x):
    return 1.0/6.0*(x**2 + 5)

# Run FIXEDPOINT
n = 7
x0 = 3.0 
xf = fixedpoint(g,x0,n)

# Print results
print("%5s %8s" % ('k','x'))
for k in range(n):
    print("%5d %9.4f" % (k+1,xf[k]))

