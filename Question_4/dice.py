import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def simulate_die_tosses(tosses, values):
    rolls = []

    for _ in range(tosses):
        rolls.append(random.choice(values))

    return rolls


if __name__ == "__main__":
    t = 10 ** 4
    n_values = [1, 2, 3, 10, 30, 100]

    Xi_mu = (1 / 17) * (1 + 4 + 6 + 8 + 9 + 10 + 12) + (2 / 17) * (2 + 3 + 5 + 7 + 11)
    Xi_variance = ((1 / 17) * (1 + 16 + 36 + 64 + 81 + 100 + 144) + (2 / 17) * (4 + 9 + 25 + 49 + 121)) - (Xi_mu ** 2)

    for n in n_values:
        Zn_samples = np.zeros(t)

        for j in range(t):
            X = simulate_die_tosses(n, [1, 4, 6, 8, 9, 10, 12] + 2 * [2, 3, 5, 7, 11])
            Zn_samples[j] = np.mean(X)

        Zn_mu = Xi_mu
        Zn_variance = Xi_variance / n
        st_dev = np.sqrt(Zn_variance)

        gaussian_samples = np.random.normal(Zn_mu, st_dev, t)

        plt.figure()
        plt.hist(Zn_samples, density=True, alpha=0.5, label='Zn')

        x = np.linspace(1, 12, 100)
        plt.plot(x, norm.pdf(x, Zn_mu, st_dev), 'r', label='Gaussian')

        plt.title(f'PDF of Zn and Gaussian for n = {n}')
        plt.xlabel('Value')
        plt.ylabel('Probability Density')
        plt.legend()
        plt.show()