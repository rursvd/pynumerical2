from numpy import zeros,array
 
def jacobi(A,b,x10,x20,x30,n):
    x1 = zeros(n)
    x2 = zeros(n)
    x3 = zeros(n)
    x1[0] = x10
    x2[0] = x20
    x3[0] = x30
    print('%7s %9s %9s %9s' % ('k','x1','x2','x3'))
    print('%7d %9.5f %9.5f %9.5f' % (0,x1[0],x2[0],x3[0]))
    for k in range(n-1):
        x1[k+1] = (b[0] - A[0,1] * x2[k] - A[0,2] * x3[k])/A[0,0]
        x2[k+1] = (b[1] - A[1,0] * x1[k] - A[1,2] * x3[k])/A[1,1]
        x3[k+1] = (b[2] - A[2,0] * x1[k] - A[2,1] * x2[k])/A[2,2]
        print('%7d %9.5f %9.5f %9.5f' % (k+1,x1[k+1],x2[k+1],x3[k+1]))
    return x1,x2,x3   

A = array([[5,-1,1],[-1,3,-1],[1,-1,4]])
b = array([6,2,11])
x10 = 0.0
x20 = 0.0
x30 = 0.0
n = 8
x1, x2, x3 = jacobi(A,b,x10,x20,x30,n)
