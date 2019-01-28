%matplotlib inline 
from numpy import linspace,sqrt
import matplotlib.pyplot as plt

x = linspace(-1,5,50)
y1 = 1.0/sqrt(x**2 + 1)
y2 = 1.0/sqrt(3 * x**2 + 1)
plt.plot(x,y1,label='plot 1')
plt.plot(x,y2,'--',label='plot 2')
plt.legend()
plt.show()
