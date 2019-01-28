from numpy import array

def simpson_data(x,y):
    nm = len(x) -1 
    h = (x[nm] - x[0])/nm
    simp = 0.0
    for i in range(1,nm):
        if (i % 2) == 1:
            simp = simp + 4.0 * y[i]
        else:
            simp = simp + 2.0 * y[i]
    simp = h * (y[0] + simp + y[nm])/3.0 
    return simp

x = array([1,2,3,4,5])
y = array([1,4,9,16,25])
T = simpson_data(x,y)
print('T = %8.4f' % T)
