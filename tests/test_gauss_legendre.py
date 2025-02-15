import numpy as np
import unittest
import matplotlib.pyplot as plt

from src.goph420_lab01.integration import integrate_gauss

class TestGauss(unittest.TestCase):

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
