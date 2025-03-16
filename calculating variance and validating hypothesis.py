import pandas as pd
import numpy as np

# File path
file_path = 'D:\data1.txt'

# Load data
cols = ['timestamp', 'open', 'high', 'low', 'close']
data = pd.read_csv(file_path, usecols=cols)

print(data.head())
print(data.info())

# Convert timestamp to datetime
data['timestamp'] = pd.to_datetime(data['timestamp'])
data = data.sort_values('timestamp')

# Calculate returns
data['Return'] = data['close'].pct_change()
print(data.head())
print(data.info())
data.dropna(subset=['Return'], inplace=True)

# Function to calculate variance ratio
def variance_ratio_test(data, window=60):
    var_1 = data['Return'].var()
    data[f'{window}_min_return'] = data['Return'].rolling(window=window).sum()
    var_window = data[f'{window}_min_return'].var()
    VR = var_window / (window * var_1)

    print(f"Variance of 1-minute returns: {var_1}")
    print(f"Variance of {window}-minute returns: {var_window}")
    print(f"Variance Ratio ({window}-minute): {VR}")

    if VR == 1:
        print("Returns likely follow a random walk (market is efficient).")
    elif VR < 1:
        print("Possible mean reversion (predictable pattern).")
    else:
        print("Possible momentum (predictable pattern).")

# Run variance ratio test
variance_ratio_test(data)
