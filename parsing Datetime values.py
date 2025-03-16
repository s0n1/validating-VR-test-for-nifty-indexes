import pandas as pd

niftyindexdata = r"__path___"





niftyindexdata = pd.read_csv(niftyindexdata)
niftyindexdata.drop(columns=[1],inplace=True)
niftyindexdata.drop(columns=[6],inplace=True)

niftyindexdata.columns = ["Datetime", "open", "high", "low", "close"]
dtype= {'0': str , 'Datetime': str, 'open': float, 'high': float, 'low': float, 'close': float, 'volume': int, 'dummy': int}
niftyindexdata["Datetime"] = pd.to_datetime(niftyindexdata["Datetime"])
niftyindexdata.set_index("Datetime", inplace=True)


print(niftyindexdata.columns) 
niftyindexdata.to_csv("__path___", sep=",", index=True, header=False, encoding='utf-8')

# print(niftyindexdata["index"])



# # Function to adjust the Datetime
def adjust_Datetime(ts):
    # Replace 'T' with a space and remove the timezone offset
    return ts.split('+')[0].replace('T', ' ')

# Apply the function to the 'Datetime' column
niftyindexdata['Datetime'] = niftyindexdata['Datetime'].apply(adjust_Datetime)

# Save the updated DataFrame to a new CSV file
niftyindexdata.to_csv(r'___path___', index=False)