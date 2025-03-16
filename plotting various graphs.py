import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Sample data structure (replace with your actual data)
data = {
    'Index': ['Nifty50', 'Nifty50', 'Nifty50', 'Nifty50',
              'Nifty100', 'Nifty100', 'Nifty100', 'Nifty100',
              'Nifty200', 'Nifty200', 'Nifty200', 'Nifty200'],
    'Interval': ['15min', '1H', '1D', '1W']*3,
    'VR_q2': [1.007, 0.985, 0.955, 1.014] + 
             [1.009, 0.985, 0.960, 1.031] + 
             [1.018, 0.992, 0.970, 1.047],
    'Spread': [4.3891, 0.0, 45.4736, 0.0] + 
              [3.1700, 0.0, 48.7415, 0.0] + 
              [0.0, 0.0, 21.9851, 0.0]
}
df = pd.DataFrame(data)

# Create subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharey=True)
sns.set_theme(style="whitegrid")

# Plot for each index
for idx, ax in zip(['Nifty50', 'Nifty100', 'Nifty200'], axes):
    # Filter data for the index
    subset = df[df['Index'] == idx]
    # Merge VR and Spread (already merged in this example)
    merged_data = subset[['Interval', 'VR_q2', 'Spread']]
    
    # Scatter plot
    sns.scatterplot(data=merged_data, x='Spread', y='VR_q2', 
                    hue='Interval', palette='viridis', 
                    s=150, ax=ax, edgecolor='black', legend=False)
    ax.axhline(1, color='black', linestyle=':', alpha=0.7)
    ax.set_title(f'{idx}', fontsize=14)
    ax.set_xlabel('Roll Spread', fontsize=12)
    ax.set_ylabel('VR(q=2)' if idx == 'Nifty50' else '', fontsize=12)
    ax.grid(True)
    
    # Annotate points with interval labels
    for _, row in merged_data.iterrows():
        ax.text(row['Spread']+0.5, row['VR_q2']+0.005, 
                row['Interval'], fontsize=9, ha='left')

plt.suptitle('VR(q=2) vs. Roll Spread Across Indices', fontsize=16, y=1.05)
plt.tight_layout()
plt.show()