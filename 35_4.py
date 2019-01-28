def fordiff(f,x,h):
    diff = (f(x+h) - f(x)) / h 
    return diff

def backdiff(f,x,h):
    diff = (f(x) - f(x-h)) / h 
    return diff

def centdiff(f,x,h):
    diff = (f(x+h) - f(x-h)) / (2.0*h) 
    return diff

def f(x):
    return x**3 -2.0*x**2 + 3*x -1.0 

x = 0.5
h = 0.25
fdiff = fordiff(f,x,h)
bdiff = backdiff(f,x,h)
cdiff = centdiff(f,x,h)
print('1st differentiation')
print('Forward difference = %8.4f' % fdiff)
print('Backward difference = %8.4f' % bdiff)
print('Central difference = %8.4f' % cdiff)
