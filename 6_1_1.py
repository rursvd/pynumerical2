%matplotlib inline
from numpy import linspace,sqrt
import matplotlib.pyplot as plt

x = linspace(-1,5,40)
y = 1.0/sqrt(x**2 + 1)
plt.plot(x,y)
plt.show()
