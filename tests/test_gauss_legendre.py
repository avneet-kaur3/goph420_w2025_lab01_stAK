import numpy as np
import unittest
import matplotlib.pyplot as plt

from src.goph420_lab01.integration import integrate_gauss

class TestGauss(unittest.TestCase):

    '''
    The following functions perform tests on the integrate_gauss function imported from the file integration.py. It tests the Gauss-Legendre Quadrature algorithm with
    the following orders: 1, 3, 5, 7 and 9. The function chosen is sin, and the interval is from 0 to pi/2.
    '''

    def test_order1(self):
        
        calculated = integrate_gauss(np.sin, [0, np.pi/2], 1)
        print(f'Order 1 result: {calculated}')

    def test_order3(self):
        calculated = integrate_gauss(np.sin, [0, np.pi/2], 2)
        print(f'Order 3 result: {calculated}')

    def test_order5(self):
        calculated = integrate_gauss(np.sin, [0, np.pi/2], 3)
        print(f'Order 5 result: {calculated}')

    def test_order7(self):
        calculated = integrate_gauss(np.sin, [0, np.pi/2], 4)
        print(f'Order 7 result: {calculated}')

    def test_order9(self):
        calculated = integrate_gauss(np.sin, [0, np.pi/2], 5)
        print(f'Order 9 result: {calculated}')

if __name__=="__main__":
    unittest.main()
