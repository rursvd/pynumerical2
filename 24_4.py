from numpy import mean,median,var,std,array

x = array([2.2, 2.3, 3.1, 3.4, 3.3, 3.2, 5])
mu = mean(x)
med = median(x)
vari = var(x)
stdd = std(x)

print('mean = %6.2f' % mu)
print('median = %6.2f' % med)
print('variance = %6.2f' % vari)
print('standard deviation = %6.2f' % stdd)
