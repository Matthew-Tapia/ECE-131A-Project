import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import sqrt


def find_mu(data_set):
    return sum(data_set) / len(data_set)


def find_sigma(data_set, mu):
    return sqrt(sum([(x_i - mu) ** 2 for x_i in data_set]) / len(data_set))


if __name__ == "__main__":
    data = np.loadtxt('data.txt')

    mean = find_mu(data)
    stddev = find_sigma(data, mean)

    print(f"Mean: {mean:.3f}")
    print(f"Standard Deviation: {stddev:.3f}")

    plt.hist(data, density=True)

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    plt.plot(x, norm.pdf(x, mean, stddev))

    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Gaussian (μ, σ) PDF and Data Histogram')
    plt.legend(['Gaussian PDF', 'Data Histogram'])
    plt.show()
