from numpy import array, zeros
from numpy.linalg import det

def cramer(A,b):
    n = len(b)
    detsub = zeros((n))
    x = zeros((n))
    detA = det(A)
    for i in range(n):
        Atemp = A.copy()
        Atemp[:,i] = b
        detsub[i] = det(Atemp)
        x[i] = detsub[i]/detA
    return detsub, x

A = array([[5,-1,1],[-1,3,-1],[1,-1,4]])
b = array([6,2,11])
detsub, x = cramer(A,b)
    
print('det(A) =  %8.4f' % det(A))
print('det(A1) =  %8.4f' % detsub[0])
print('det(A2) =  %8.4f' % detsub[1])
print('det(A3) =  %8.4f' % detsub[2])
print('x1 = %8.4f' % x[0])
print('x2 = %8.4f' % x[1])
print('x3 = %8.4f' % x[2])
