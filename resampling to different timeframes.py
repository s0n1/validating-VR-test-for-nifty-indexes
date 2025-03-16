import pandas as pd

nifty50 = r"D:\paper\data_nifty200.csv"

df = pd.read_csv(nifty50)

print(df.head())

df['Datetime'] = pd.to_datetime(df['Datetime'])
df.set_index('Datetime', inplace=True)

agg_methods = {
    'open': 'first',   # First price in the 5-minute window
    'high': 'max',     # Maximum price during the window
    'low': 'min',      # Minimum price during the window
    'close': 'last',   # Last price in the window  
}

# Resample and aggregate
df_min = df.resample('W-FRI').agg(agg_methods).dropna()  ### W-FRI for one week

print(df_min.head())

df_min.to_csv(r"D:\paper\nifty200\1week_nifty200.csv", sep=",", index=True, header=True, encoding='utf-8')

