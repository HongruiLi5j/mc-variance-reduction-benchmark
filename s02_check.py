from bs import bs_price
from mc import mc_call_price

S0, K, r, sigma, T = 100, 100, 0.05, 0.2, 1.0
price, se = mc_call_price(S0, K, r, sigma, T, n=1_000_000, seed=0)
exact = bs_price(S0, K, r, sigma, T, "call")
print("MC price:", price)
print("std error:", se)
print("exact BS:", exact)
print("within 3 standard errors:", abs(price - exact) < 3 * se)
