import numpy as num
import matplotlib.pyplot as plt
import numpy as np
from math import comb
from scipy.integrate import quad


class BinomialDistribution:
    def __init__(self, n: int, p: float):
        self.n = n
        self.p = p
        self.probabilities = []
        for num in range(n + 1):
            self.probabilities.append(self.binomial_distribution(self.n, self.p, num))
        # print(self.probabilities)
        plt.bar(range(n + 1), self.probabilities)
        plt.ylabel('Probability')
        plt.xlabel('Number of Successes')
        plt.title('Binomial Distribution')
        plt.bar_label(plt.bar(range(n + 1), self.probabilities))
        plt.show()

    def binomial_distribution(self, n, p, k):
        nCk = comb(self.n, k)
        probSuccess = (self.p) ** k
        probFail = (1 - self.p) ** (self.n - k)
        return probSuccess * probFail * nCk


class BernoulliDistribution:
    def __init__(self, p: float, attempt_list: []):
        self.p = p
        self.success_count = 0
        self.fail_count = 0
        for attempt in attempt_list:
            if attempt == 1:
                self.success_count += 1
            else:
                self.fail_count += 1
        print(self.calculate_bernoulli())

    def calculate_bernoulli(self):
        return self.p ** (self.success_count) * (1 - self.p) ** (self.fail_count)


class GeometricDistribution:
    def __init__(self, p: float):
        self.p = p

    def geometric_distribution(self, k):
        return (1 - self.p) ** (k - 1) * self.p

class NormalDistribution:
    def __init__(self, mu: float, sigma: float):
        self.mu = mu
        self.sigma = sigma
        self.x = num.linspace(-10, 10, 100)
        self.y = (1 / (self.sigma * num.sqrt(2 * num.pi))) * num.exp(-0.5 * ((self.x - self.mu) / self.sigma) ** 2)
        plt.plot(self.x, self.y)
        plt.xlabel('x')
        plt.ylabel('Probability Density')
        plt.title('Normal Distribution')
        plt.grid(True)
        plt.show()

    def area(self, a: float, b: float, xlim: []=None):
        def integrand(x):
            return (1 / (self.sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - self.mu) / self.sigma) ** 2)
        if(xlim is not None):
            plt.xlim(xlim)
        area, _ = quad(integrand, a, b)
        plt.fill_between(self.x, self.y, where=(self.x >= a) & (self.x <= b), color='skyblue')
        plt.plot(self.x, self.y)
        plt.text((a + b) / 2, 0.1, f'Area: {area:.2f}', ha='center', fontsize=12)
        plt.xlabel('x')
        plt.ylabel('Probability Density')
        plt.title('Normal Distribution with Area')
        plt.grid(True)
        plt.show()

class NormalApproximation:
    def __init__(self, n: float, p:int, xlim: [] = None):
        self.n = n
        self.p = p
        self.mu = self.n * self.p
        self.sigma = num.sqrt(self.n * self.p * (1 - self.p))
        if self.sigma < 10:
            print("The normal approximation is not accurate because the sample size is too small.")
        self.x = num.linspace(0, self.n, 100)
        self.y = (1 / (self.sigma * num.sqrt(2 * num.pi))) * num.exp(-0.5 * ((self.x - self.mu) / self.sigma) ** 2)
        plt.plot(self.x, self.y)
        if(xlim is not None):
            plt.xlim(xlim)
        plt.xlabel('x')
        plt.ylabel('Probability Density')
        plt.title('Normal Approximation')
        plt.grid(True)
        plt.show()

def main():
    ##coin_flip_10_times = BinomialDistribution(7, .5)
    ##coin_flip_0001 = BernoulliDistribution(.5, [0, 0, 0, 1])
    ##coin_flip_until_heads = GeometricDistribution(.5)
    ##coin_flip_until_heads.geometric_distribution(3)
    ##normal_musig = NormalDistribution(0, 1)
    ##normal_musig.area(-1, 1, xlim=[-3,3])
    normal_aprox = NormalApproximation(100, .5, xlim=[30, 70])



if __name__ == '__main__':
    main()
