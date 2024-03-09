import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


if __name__ == "__main__":
    t = 10 ** 4
    n_values = [1, 2, 3, 10, 30, 100]

    for n in n_values:
        Zn_samples = np.zeros(t)

        for j in range(t):
            X = np.random.uniform(10, 16, n)
            Zn_samples[j] = np.mean(X)

        mu = 13
        variance = 3/n
        st_dev = np.sqrt(variance)

        gaussian_samples = np.random.normal(mu, st_dev, t)

        plt.figure()
        plt.hist(Zn_samples, density=True, alpha=0.5, label='Zn')

        x = np.linspace(mu - 3 * st_dev, mu + 3 * st_dev, 100)
        plt.plot(x, norm.pdf(x, mu, st_dev), 'r', label='Gaussian')

        plt.title(f'PDF of Zn and Gaussian for n = {n}')
        plt.xlabel('Value')
        plt.ylabel('Probability Density')
        plt.legend()
        plt.show()
