import numpy as np
from bs import bs_price

S0, K, r, sigma, T = 100, 100, 0.05, 0.2, 1.0
c = bs_price(S0, K, r, sigma, T, "call")
p = bs_price(S0, K, r, sigma, T, "put")
print(f"call = {c:.4f}, put = {p:.4f}")
print("put-call parity gap:", c - p - (S0 - K * np.exp(-r * T)))