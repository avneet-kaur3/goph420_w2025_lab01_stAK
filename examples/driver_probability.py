import numpy as np
import matplotlib.pyplot as plt

from goph420_lab01.integration import (
    integrate_gauss,
    )

def main():

    #Defining the standard normal probability density function.
    def f(x):
        return (1/np.sqrt(2 * np.pi)) * np.exp((-1/2) * ((x - mean)/std)**2)
    
    integral_gauss = []
    probability = []
    length_probability = []

    for n in range(1, 6):
        #Defining the constants for the question.
        z = 4.0
        mean = 1.5
        std = 0.5
        #The integral must be done in two parts - from minus infinity to zero, which has a given value of 0.5, and from 0 to z.
        integral_gauss.append(integrate_gauss(f, [0, z], n) + 0.5)
        probability.append(1 - (integrate_gauss(f, [0, z], n) + 0.5))

    for n in range(1, 6):
        #Defining the constants for the question.
        mean = 10.28
        std = 0.05
        #The integral must be done in two parts - from minus infinity to zero, which has a given value of 0.5, and from 0 to z.
        length_probability.append(integrate_gauss(f, [10.25, 10.35], n))

    #Converting the empty list to a numpy array to calculate the relative error.
    length_probability = np.array(length_probability)
    probability = np.array(probability)

    #Calculating the relative error between them for convergence.
    error_seismic = np.abs((probability[:-1] - probability[1:])/probability[:-1])
    error_length = np.abs((length_probability[:-1] - length_probability[1:])/length_probability[:-1])

    plt.loglog(points, error_seismic, label = 'Relative Seismic Probability Error')
    plt.loglog(points, error_length, label = 'Relative Length Error')

    plt.xlabel('sampling points, npts')
    plt.ylabel('relative error, εa')
    plt.legend()

    plt.savefig(r'C:\Users\HP\Desktop\University Courses\Winter 2025\GOPH 420\goph420_w2025_lab01_stAK\figures\gauss_quadrature_error.png')


if __name__ == "__main__":
    main()