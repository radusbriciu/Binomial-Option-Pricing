# =============================================================================
# Plain European Binomial Option Pricing
# (on a non-dividend-paying stock)
# =============================================================================

import numpy as np

# =============================================================================
# Input Parameters
# =============================================================================

S0 = 100 # Price at inception
r = 0.03 # Risk-free rate
u = 0.2 # Size of an up movemnent (exponential return)
d = -0.1 # Size of a down movement (exponential return)
T = 2 # Time to maturity
n = 2 # Number of time steps
K = 90 # Strike

# =============================================================================
# Calculated Parameters
# =============================================================================

dt = T/n 
    # Increment of time step
qu = (np.exp(r*dt)-np.exp(d*dt))/(np.exp(u*dt)-np.exp(d*dt)) 
    # Risk neutral Probability of an up movement
qd = 1-qu
    # Risk neutral Probability of a down movement

# =============================================================================
# Call
# =============================================================================

C = np.zeros((n+1,1))

for i in range(0,n+1):
    C[i] = qu**i * qd**(n-i) * np.maximum(S0 * np.exp(u*i + d*(n-i)) - K, 0)

C0 = np.exp(-r*T) * np.sum(C)

print(np.round(C0,2))

# =============================================================================
# Put
# =============================================================================

P = np.zeros((n+1,1))

for i in range(0,n+1):
    P[i] = qu**i * qd**(n-i) * np.maximum(K - S0 * np.exp(u*i + d*(n-i)), 0)

P0 = np.exp(-r*T) * np.sum(P)

print(np.round(P0,2))
