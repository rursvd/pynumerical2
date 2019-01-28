%matplotlib inline
from numpy import array
import matplotlib.pyplot as plt

time = array([1,2,3,4,5,6,7])
temp = array([20,23,25,22,21,19,18])

plt.plot(time,temp,'k')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.show()
