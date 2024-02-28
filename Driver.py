from NamedDistributions import BinomialDistribution, BernoulliDistribution, GeometricDistribution

def main():
    while True:
        print("Welcome to the Named Distributions program!")
        print("1. Binomial Distribution")
        print("2. Bernoulli Distribution")
        print("3. Geometric Distribution")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if(input == 1):
            pass
        elif(input == 2):
            pass
        elif(input == 3):
            pass
        elif(input == 4):
            pass
        else:
            print("Invalid choice! Please try again.")

def binomial_distribution_handler():
    n = int(input("Enter the number of trials: "))
    p = float(input("Enter the probability of success: "))
    binomial = BinomialDistribution(n, p)

def bernoulli_distribution_handler():
    pass

def geometric_distribution_handler():
    pass

if __name__ == '__main__':
    main()