from numpy import array, sqrt, zeros, set_printoptions

def cholesky(A,b):
    # Lower triangular matrix
    el = zeros((3,3))
    el[0,0] = sqrt(A[0,0])
    el[1,0] = A[1,0] / el[0,0]
    el[1,1] = sqrt(A[1,1] - el[1,0]**2)
    el[2,0] = A[2,0] / el[0,0]
    el[2,1] = (A[2,1] - el[2,0] * el[1,0])/el[1,1]
    el[2,2] = sqrt(A[2,2] - el[2,0]**2 - el[2,1]**2)
    # Forward substitution for y
    y = zeros((3))
    y[0] = b[0] / el[0,0]
    y[1] = (b[1] - el[1,0] * y[0]) / el[1,1]
    y[2] = (b[2] - el[2,0] * y[0] - el[2,1] * y[1]) / el[2,2]
    # Backward substitution for x
    x = zeros((3))
    elT = el.T
    x[2] = y[2] / elT[2,2] 
    x[1] = (y[1] - elT[1,2] * x[2]) / elT[1,1]
    x[0] = (y[0] - elT[0,1] * x[1] - elT[0,2] * x[2]) / elT[0,0]   
    return el, y, x

# Input parameters to choesky(A,b) function
A = array([[5,-1,1],[-1,3,-1],[1,-1,4]])
b = array([6,2,11])
el, y, xc = cholesky(A,b)

set_printoptions(precision = 4)
print("L = ", el)
print("y = ", y)
print("x1 = %8.4f " % xc[0])
print("x2 = %8.4f " % xc[1])
print("x3 = %8.4f " % xc[2])
