import numpy


def mrt(f, a, b, eps):
    """ Calculate the integral of f from a to b using the midpoint rule.
    
    Parameters
    ----------
    func : callable
        The function to integrate.
    a : float
        The lower limit of integration.
    b : float
        The upper limit of integration.
    eps : float
        The target accuracy of the estimate.
        
    Returns
    -------
    integral : float
        The estimate of $\int_a^b f(x) dx$.
    niter : int
        number of iterations
    """
    i = 2
    Q_prev = f(a/2+b/2)*(b-a)
    while True:
        dots = numpy.linspace(a,b,2**i)
        points = (dots[1:]+dots[:-1])/2
        h = dots[1]-dots[0]
        Q_curr = h*numpy.sum(f(points))
        if abs(Q_curr-Q_prev)<eps:
            return [Q_curr, i]
        Q_prev = Q_curr
        i +=1
