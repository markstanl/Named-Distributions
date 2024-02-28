# Named Distributions
The following is a collection of named distributions.
As a scholar taking Introduction to the Theory of Probability,
 I have decided to compile a program that computes all of the named
distributions that we have learned in class.
## Bernoulli Distribution
The Bernoulli distribution is a discrete distribution with two possible outcomes labeled by 0 and 1. It is a special case of the binomial distribution where a single trial is conducted (n=1).
The PMF of the Bernoulli distribution is given by:  
P(X=1) = p  
P(X=0) = 1-p  
Where p is the probability of success.
Denoted by X ~ B(p)  
My program takes in a list of successes and failures (as 1s and 0s) and returns the probability of success of that configuration.
## Binomial Distribution
The binomial distribution is a discrete distribution with two possible outcomes labeled by 0 and 1. It is similar
to the Bernoulli distribution, but instead of a single trial, the binomial distribution consists of n independent trials.
The PMF of the binomial distribution is given by:  
P(X=k) = (n choose k) * p^k * (1-p)^(n-k)  
Where n is the number of trials, k is the number of successes, and p is the probability of success.  
Denoted by X ~ B(n,p)
## Geometric Distribution
The geometric distribution is a discrete distribution that models the number of trials needed to achieve the first success in a sequence of independent Bernoulli trials.  
The PMF of the geometric distribution is given by:  
P(X=k) = (1-p)^(k-1) * p    
Where k is the number of trials needed to achieve the first success, and p is the probability of success.
Denoted by X ~ G(p)