import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def hp_filter(src, lambd=100):
    trend = [np.nan] * len(src)
    trend[0] = src[0]

    for i in range(1, len(src)):
        trend[i] = (src[i] + (lambd - 1) * (trend[i - 1] if not np.isnan(trend[i - 1]) else src[i])) / lambd

    return pd.Series(trend, index=src.index)

stock_symbol = '^FTW5000'
lambda_value = 35
display_mode = "Percentage"

# Download data
data = yf.download(stock_symbol, start="2023-01-01", end="2024-11-04")
data['Close'] = data['Adj Close']

# Calculate HP Filter trend
data['HP_Trend'] = hp_filter(data['Close'], lambda_value)
data['Cycle_Pct'] = (data['Close'] - data['HP_Trend']) / data['HP_Trend'] * 100
data['Cycle_Price'] = data['Close'] - data['HP_Trend']

# Calculate median values for positive and negative cycles
positive_cycles = data['Cycle_Pct'][data['Cycle_Pct'] > 0]
negative_cycles = data['Cycle_Pct'][data['Cycle_Pct'] < 0]

pos_median = positive_cycles.mean() if not positive_cycles.empty else 0
neg_median = negative_cycles.mean() if not negative_cycles.empty else 0

# Calculate target levels
data['Long_Target'] = data['HP_Trend'] * (1 + pos_median/100)
data['Short_Target'] = data['HP_Trend'] * (1 + neg_median/100)

# Create the plot
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios': [3, 1]}, figsize=(12, 8))

# Plot price and trends
ax1.plot(data.index, data['Close'], label='Close Price', color='black', linewidth=1)
ax1.plot(data.index, data['HP_Trend'], label='HP Filter (Trend)', color='blue', linestyle='-', linewidth=0.8)
ax1.plot(data.index, data['Long_Target'], label='Positive Median Trend', color='green', linestyle='-', linewidth=0.8)
ax1.plot(data.index, data['Short_Target'], label='Negative Median Trend', color='red', linestyle='-', linewidth=0.8)
ax1.set_title(f"{stock_symbol} Price and HP Filter Trend")
ax1.set_ylabel('Price')
ax1.legend()
ax1.grid()

# Plot cycle component
if display_mode == "Percentage":
    ax2.plot(data.index, data['Cycle_Pct'], label='HP Filter Divergence (%)', color='blue', linewidth=1)
    ax2.axhline(pos_median, color='green', linestyle='--', label=f'Positive Median ({pos_median:.2f}%)')
    ax2.axhline(neg_median, color='red', linestyle='--', label=f'Negative Median ({neg_median:.2f}%)')
    ax2.set_ylabel('Divergence (%)')
else:
    ax2.plot(data.index, data['Cycle_Price'], label='HP Filter Divergence (Price)', color='blue', linewidth=1)
    ax2.set_ylabel('Divergence (Price)')

ax2.axhline(0, color='gray', linestyle='--', linewidth=0.5)
ax2.set_title("HP Filter Divergence")
ax2.legend()
ax2.grid()

plt.xlabel('Date')
plt.tight_layout()
plt.show()

# Print statistics
print(f"\nCycle Statistics:")
print(f"Positive Median: {pos_median:.2f}%")
print(f"Negative Median: {neg_median:.2f}%")