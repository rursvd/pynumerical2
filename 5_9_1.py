from numpy import linspace, zeros,sin

x = linspace(0,2,10) 
n = len(x)
y = zeros(n) 

for i in range(n):
    y[i] = sin(x[i])
    print('%8.4f ' % y[i])
