%matplotlib inline
from numpy import array
import matplotlib.pyplot as plt 

height = array([ 8.2,8.1 ,9.1,6.3,7.6,8.1,6.5,5.5,9.1,8.3])

plt.hist(height,color='black')
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.show()
