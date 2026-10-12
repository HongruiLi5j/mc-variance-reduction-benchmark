"""Black-Scholes closed-form price (European option, no dividends)"""
import numpy as np
from scipy.stats import norm


def d1_d2(S0, K, r, sigma, T):
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    return d1, d1 - sigma * np.sqrt(T)


def bs_price(S0, K, r, sigma, T, kind="call"):
    d1, d2 = d1_d2(S0, K, r, sigma, T)
    if kind == "call":
        return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    if kind == "put":
        return K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
    raise ValueError("kind must be 'call' or 'put'")