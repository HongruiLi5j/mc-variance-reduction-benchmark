import numpy as np


def mc_call_price(S0, K, r, sigma, T, n, seed):
    rng = np.random.default_rng(seed)
    Z = rng.standard_normal(n)
    S_T = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(S_T - K, 0)
    discounted = np.exp(-r * T) * payoff
    price = discounted.mean()
    stderr = discounted.std(ddof=1) / np.sqrt(n)
    return price, stderr