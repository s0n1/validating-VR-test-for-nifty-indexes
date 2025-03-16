import pandas as pd  
import seaborn as sns  

# Load cleaned data (e.g., Nifty 50 15-minute returns)  
df = pd.read_csv(r'D:\paper\nifty50\15min_nifty50.csv')  
df.rename(columns={'0': 'Datetime',   '1': 'open',   '2': 'close',  '3': 'high',   '4': 'low'}, inplace=True)
print(df.head)

# Calculate key statistics  
desc_stats = df['return'].describe(percentiles=[0.01, 0.05, 0.95, 0.99])  
desc_stats['skewness'] = df['return'].skew()  
desc_stats['kurtosis'] = df['return'].kurtosis()  

# Amihud Illiquidity Ratio (example)  
df['illiq'] = abs(df['return']) / df['volume']  
amihud_ratio = df['illiq'].mean()  

# Print results  
print(desc_stats)  
print(f'Amihud Ratio: {amihud_ratio:.2e}')  