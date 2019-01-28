from numpy import array,zeros,append
import numpy as np

def gausselim(A,b):
   #AUGMENTED MATRIX
    augA = np.c_[A,b]
    p1 = augA [1,:] - augA [0,:] * (augA [1,0]/augA [0,0]) 
    p2 = augA [2,:] - augA [0,:] * (augA [2,0]/augA [0,0])
    temp = append(augA[0,:],p1)
    augA1 = append(temp,p2).reshape(3,4)  
    p3 = augA1[2,:] - augA1[1,:] * (augA1[2,1]/augA1[1,1]) 
    augA2 = augA1.copy() 
    augA2[2] = p3
    A = augA2[:,0:3]
    b = augA2[:,-1]
    print("A = ",A)
    print("b = ",b)
    # BACK SUBSTITUTION
    x = zeros((3))
    x[2] = b[2]/A[2,2]
    x[1] = (b[1] - A[1,2] * x[2])/A[1,1] 
    x[0] = (b[0] - A[0,2] * x[2] - A[0,1] * x[1])/A[0,0]  
    return x

A = array([[5,-1,1],[-1,3,-1],[1,-1,4]])
b = array([6,2,11])
xg = gausselim(A,b)    
    
print('x1 = %8.4f' % xg[0])
print('x2 = %8.4f' % xg[1])
print('x3 = %8.4f' % xg[2])
