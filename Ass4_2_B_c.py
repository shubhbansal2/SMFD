import numpy as np
from scipy.stats import norm
from scipy.integrate import quad

# Parameters
S0 = 100
K = 105
sigma_10 = 1.253 * np.sqrt(10) 

# Integral
def integral(S):
    return (S - K) * norm.pdf(S, loc=S0, scale=sigma_10)

# Integrate from K to infinity
expected_payoff, error = quad(integral, K, np.inf)

print(f"Expected Payoff: {expected_payoff:.4f}")
