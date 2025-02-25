import numpy as np
import unittest
import matplotlib.pyplot as plt

from src.goph420_lab01.integration import integrate_newton

class TestNewton(unittest.TestCase):

    '''
    The following functions perform tests on the integrate_newton function imported from the file integration.py. It tests the Trapezoidal Rule and Simpson's
    1/3 Rule algorithms with a linear function for the Trapezoidal Rule and a quadratic function for the Simpson's Rule. The tests for the Simpson's Rule also consider
    an odd number of data points and an even number of data points.
    '''

    def test_trapezoidal(self):
        x = np.linspace(0, 10, 101)
        f = (5*x) + 10
        calculated = integrate_newton(x, f, 'trap')
        print(f'Trapezoidal result: {calculated}')

    def test_simpsons_even(self):
        x = np.linspace(0, 10, 100)
        f = (5*(x**2)) + x + 10
        calculated = integrate_newton(x, f, 'simp')
        print(f'Simpson\'s result with even number of data points: {calculated}')

    def test_simpsons_odd(self):
        x = np.linspace(0, 10, 101)
        f = (5*(x**2)) + x + 10
        calculated = integrate_newton(x, f, 'simp')
        print(f'Simpson\'s result with odd number of data points: {calculated}')

if __name__=="__main__":
    unittest.main()

