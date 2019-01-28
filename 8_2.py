from numpy import zeros, sign

# Define bisection function
def bisection(f,a,b,n):
    c = zeros(n)
    for i in range(n):
        c[i] = (a + b)/2.0
        if sign(f(c[i])) == sign(f(a)):
            a = c[i]
        else:
            b = c[i]
    return c

# Define function
def f(x): 
    return -x**2 + 6.0 * x - 5.0

# Execute bisection function
a = -2.0
b = 3.0
n = 7
xb = bisection(f,a,b,n)

# Print results
print("%5s %8s" % ('k','c'))
for k in range(n):
    print("%5d %9.4f" % (k+1,xb[k]))
