import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

niftydata = r"D:\paper\data\15min_nifty200.csv"
# Load cleaned data (e.g., Nifty 50 15-minute returns)  
df = pd.read_csv(niftydata)
# df.columns = ["Datetime", "open", "high", "low", "close"]
# print(df.head())

df['log_return'] = np.log(df['close'] / df['close'].shift(1))  
df.dropna(inplace=True)  # Remove first NaN 

def variance_ratio(returns, q):
    n = len(returns)
    mu = np.mean(returns)
    
    # 1-period variance
    var_1 = np.sum((returns - mu)**2) / (n - 1)
    
    # q-period variance (overlapping)
    returns_q = returns.rolling(q).sum().dropna()
    var_q = np.sum((returns_q - q*mu)**2) / (len(returns_q) - 1)
    
    # Variance ratio
    vr = var_q / (q * var_1)
    return vr

def lo_mackinlay_statistic(returns, q):
    n = len(returns)
    vr = variance_ratio(returns, q)
    nq = len(returns.rolling(q).sum().dropna())
    mu = np.mean(returns)
    var_1 = np.sum((returns - mu)**2) / (n - 1)
    # Compute theta(q) with heteroskedasticity adjustment
    delta = []
    for j in range(1, q):
        prod = (returns[j:] - mu) * (returns[:-j] - mu)
        delta_j = np.sum(prod**2) / (nq * var_1**2)
        delta.append(delta_j)
    
    theta = sum([(2*(q - j)/q)**2 * dj for j, dj in enumerate(delta, 1)])
    m = (vr - 1) / np.sqrt(theta)
    return m

# Example for q = 2, 5, 10
q_values = [2, 5, 10]
results = []

for q in q_values:
    vr = variance_ratio(df['log_return'], q)
    m = lo_mackinlay_statistic(df['log_return'], q)
    results.append({'q': q, 'VR': vr, 'M(q)': m})

results_df = pd.DataFrame(results)
print(results_df)

# Compute price changes
df['delta_p'] = df['close'].diff().dropna()

# Calculate serial covariance
gamma = df['delta_p'].autocorr(lag=1) * df['delta_p'].var()

# Roll spread (ensure gamma is negative)
if gamma < 0:
    spread = 2 * np.sqrt(-gamma)
else:
    spread = 0

print(f"Roll Spread: {spread:.4f}")

# Critical values
critical_value_5pct = 1.96  # For single q
chow_denning_cv = 2.49      # For multiple q-values

# Evaluate results
results_df['Reject H0 (5%)'] = np.abs(results_df['M(q)']) > critical_value_5pct
results_df['CD Reject H0'] = np.abs(results_df['M(q)']).max() > chow_denning_cv

print(results_df)

