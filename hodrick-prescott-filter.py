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

stock_symbol = 'AAPL'
lambda_value = 35
display_mode = "Percentage"

data = yf.download(stock_symbol, start="2023-01-01", end="2024-11-04")
data['Close'] = data['Adj Close']

data['HP_Trend'] = hp_filter(data['Close'], lambda_value)
data['Cycle_Pct'] = (data['Close'] - data['HP_Trend']) / data['HP_Trend'] * 100
data['Cycle_Price'] = data['Close'] - data['HP_Trend']

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios': [3, 1]}, figsize=(12, 8))

ax1.plot(data.index, data['Close'], label='Close Price', color='black', linewidth=1)
ax1.plot(data.index, data['HP_Trend'], label='HP Filter (Trend)', color='orange', linestyle='-')
ax1.set_title(f"{stock_symbol} Price and HP Filter Trend")
ax1.set_ylabel('Price')
ax1.legend()
ax1.grid()

if display_mode == "Percentage":
    ax2.plot(data.index, data['Cycle_Pct'], label='HP Filter Divergence (%)', color='red', linewidth=1.5)
    ax2.set_ylabel('Divergence (%)')
else:
    ax2.plot(data.index, data['Cycle_Price'], label='HP Filter Divergence (Price)', color='blue', linewidth=1.5)
    ax2.set_ylabel('Divergence (Price)')

ax2.axhline(0, color='gray', linestyle='--', linewidth=0.5)
ax2.set_title("HP Filter Divergence")
ax2.legend()
ax2.grid()

plt.xlabel('Date')
plt.tight_layout()
plt.show()
