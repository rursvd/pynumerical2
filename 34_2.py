from numpy import array,exp,sqrt

def gaussquad(f,n):
    if (n==4):
        # n = 4 Guassian quadrature
        wi = array([0.6521451548625461,0.6521451548625461,
                    0.3478548451374538,0.3478548451374538])
        xi = array([-0.3399810435848563,0.3399810435848563,
                    -0.8611363115940526,0.8611363115940526])
    elif (n==3):
        # n = 3 Guassian quadrature
        wi = array([0.8888888888888888, 0.5555555555555556, 
                    0.5555555555555556])
        xi = array([0.0000000000000000, -0.7745966692414834, 
                    0.7745966692414834])    
    else:
        # n = 2 Guassian quadrature
        wi = array([1.0,1.0])
        xi = array([-0.5773502691896257,0.5773502691896257])
    gauss = 0.0
    for i in range(n):
        gauss = gauss + wi[i]*f(xi[i])
    return gauss  

def f(x):
    return x**2*exp(-x)/sqrt(1.0 + x**2)

n = 2
gquad = gaussquad(f,n)
