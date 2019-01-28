%matplotlib inline 
from numpy import array
import matplotlib.pyplot as plt

x = array([0,1,3,7,8])
y = array([1.1,2.5,-0.7,3.0,2.9])
plt.plot(x,y,'o-')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
