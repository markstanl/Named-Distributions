import numpy as num
import matplotlib.pyplot as plt
from math import comb


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


def main():
    coin_flip_10_times = BinomialDistribution(7, .5)
    coin_flip_0001 = BernoulliDistribution(.5, [0, 0, 0, 1])
    coin_flip_until_heads = GeometricDistribution(.5)
    coin_flip_until_heads.geometric_distribution(3)


if __name__ == '__main__':
    main()
