import numpy as np
import matplotlib.pyplot as plt

from src.goph420_lab01.integration import integrate_newton

def main():
    #Loading seismic data.
    data = np.loadtxt('examples/s_wave_data.txt')
    t_data = data[:, 0]
    v_data = data[:, 1]
    v_squared_data = v_data**2

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 1, 1)
    plt.plot(t_data, v_data, label = 's_wave_data')
    plt.xlabel('time, t (s)')
    plt.ylabel('velocity, v (m/s)')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(t_data, v_squared_data, label = 's_wave_data')
    plt.xlabel('time, t (s)')
    plt.ylabel('velocity squared, v^2 (m/s)^2')
    plt.legend()

    plt.savefig(r'C:\Users\HP\Desktop\University Courses\Winter 2025\GOPH 420\goph420_w2025_lab01_stAK\figures\s_wave_data.png')

    #Defining sampling intervals to downsample the data for convergence plots.
    sampling_intervals = [0.01, 0.02, 0.04, 0.08]

    #Defining empty lists to store the estimated integral values from the trapezoid method and the Simpson's method.
    trapezoidal_integral = []
    simpsons_integral = []

    for n in sampling_intervals:
        t_sampled = t_data[::int(1/n)]
        v_sampled = v_data[::int(1/n)]

        trapezoidal_integral.append((1/10) * integrate_newton(t_data, v_squared_data, 'trap'))
        simpsons_integral.append((1/10) * integrate_newton(t_data, v_squared_data, 'simp'))

    #Converting the empty list to a numpy array to calculate the relative error.
    trapezoidal_integral = np.array(trapezoidal_integral)
    simpsons_integral = np.array(simpsons_integral)

    #Calculating the relative error between them for convergence.
    error_trapezoid = np.abs((trapezoidal_integral[:-1] - trapezoidal_integral[1:])/trapezoidal_integral[:-1])
    error_simpsons = np.abs((simpsons_integral[:-1] - simpsons_integral[1:])/simpsons_integral[:-1])

    plt.figure(figsize=(12, 8))

    plt.loglog(sampling_intervals, error_trapezoid, label = 'Relative Trapezoid Rule Error')
    plt.loglog(sampling_intervals, error_simpsons, label = 'Relative Simpsons Rule Error')

    plt.xlabel('sampling interval, dt (s)')
    plt.ylabel('relative error, εa')
    plt.legend()

    plt.savefig(r'C:\Users\HP\Desktop\University Courses\Winter 2025\GOPH 420\goph420_w2025_lab01_stAK\figures\newton_methods_error.png')


if __name__ == "__main__":
    main()