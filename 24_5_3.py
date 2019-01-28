%matplotlib inline
from numpy import array
import matplotlib.pyplot as plt

pH = array([2.2, 2.3, 3.1, 3.4, 3.3, 3.2, 5])
weight = array([81,80,85,83,82,87,92])

plt.scatter(weight,pH,s=90,facecolor='black')
plt.xlabel('Weight')
plt.ylabel('pH')
plt.show()
