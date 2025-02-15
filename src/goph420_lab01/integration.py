import numpy as np
import matplotlib.pyplot as plt


def integrate_newton(x, f, alg = 'trap'):
    '''Approximates the integral of f(x) over a set time period from 0 to 10 seconds by Newton-Cotes rules.
    The function can carry out the integration through the trapezoid rule or the 1/3 Simpson's rule.
    The default value for the alg flag set is 'trap'.

    Parameters: 
        x (array_like) : Coordinates of the sample points.
        f (array_like) : Values of the function at the sample points.
        alg (str) : Flag for the algorithm to be used.
    Returns: 
        integral (float) : Provides a floating point value for the integral estimate.
    '''
    #If the value of alg given is not 'trap' or 'simp', a ValueError will be raised.
    if (alg.strip().lower() not in ['trap', 'simp']):
        raise ValueError("The algorithm chosen must be 'trap' or 'simp'.")
    
    #If the x and f arrays are incompatible, respective ValueErrors will be raised.
    if (x.shape[0] != f.shape[0]):
        raise ValueError('Arrays x and f have different lengths.')
    if (x.ndim != 1) or (f.ndim != 1):
        raise ValueError('Arrays x and f must be one-dimensional.')

    #Defining the step size of the coordinates by taking the difference between the first two.
    dx = x[1] - x[0]

    #Placing conditional statements based whether the chosen algorithm is trapezoid rule or simpson's 1/3 rule.
    if(alg == 'trap'):
        integral = (dx/2) * np.sum(f[1:] + f[:-1])

    elif(alg == 'simp'):
        integral = (dx/3) * (f[0] + f[-1] + (4 * np.sum(f[1:-1:2])) + (2 * np.sum(f[2:-2:2])))

    return integral


def integrate_gauss(f, lims, npts = 3):
    '''Approximates the integral of f(x) over a set time period from 0 to 10 seconds by Newton-Cotes rules.
    The function can carry out the integration through the trapezoid rule or the 1/3 Simpson's rule.
    The default value for the alg flag set is 'trap'.

    Parameters: 
        f : Reference to a callable object.
        lims (object) : Lower and upper bounds of the integration.
        npts (integer) : Number of integration points to us.
    Returns: 
        integral (float) : Provides a floating point value for the integral estimate.
    '''

    #If f is not callable, a TypeError will be raised.
    if not callable(f):
        raise TypeError('Parameter f must be a callable function.')

    #If the length of lims is not 2, a ValueError will be raised.
    if (len(lims) != 2):
        raise ValueError("The lims parameter requires a length of two - upper and lower parameters.")

    #If the upper and lower limits of the integral cannot be converted to float, a ValueError will be raised.
    try:
        float(lims[0]), float(lims[1])
    except ValueError:
        raise ValueError("The lims parameter must have values that are convertible to float.")

    #If npts is not in [1, 2, 3, 4, 5], a ValueError will be raised.
    if npts not in [1, 2, 3, 4, 5]:
        raise ValueError('Parameter npts must be in [1, 2, 3, 4, 5].')

    #Getting the sample points and weights for the Gauss-Legendre quadrature.
    x_k, w = np.polynomial.legendre.legauss(npts)
    #The function above only works for an interval of [-1, 1]. Values are translated to the actual limits.
    x = 0.5*(x_k + 1)*(lims[1] - lims[0]) + lims[0]
    #Calculating the integral.
    integral = np.sum(w * f(x)) * 0.5 * (lims[1] - lims[0])

    return integral

