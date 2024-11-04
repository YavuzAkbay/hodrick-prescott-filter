# 📈 Stock Price Trend Analysis with HP Filter

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python tool that analyzes stock price trends using the Hodrick-Prescott filter, separating trend components from cyclical fluctuations in financial time series data.

## 🚀 Features

- 📊 Downloads historical stock data via `yfinance`
- 📉 Implements Hodrick-Prescott filter for trend decomposition
- 📈 Calculates price divergence from trend
- 🎨 Creates publication-quality visualizations
- ⚙️ Configurable parameters for analysis customization

## 📋 Prerequisites

Before running the script, ensure you have Python 3.7+ installed on your system.

## 🔧 Installation

1. Clone the repository
```bash
git clone https://github.com/YavuzAkbay/hodrick-prescott-filter
cd hodrick-prescott-filter
```

2. Install required packages
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Basic usage with default parameters:
```python
python stock_analysis.py
```

2. Customize analysis parameters in the script:
```python
stock_symbol = 'AAPL'      # Stock ticker symbol
lambda_value = 35          # HP filter smoothing parameter
display_mode = "Percentage"  # Display mode ("Percentage" or "Price")
```

## 📊 Example Output

The script generates a two-panel visualization:
- Top panel: Stock price with HP trend line
- Bottom panel: Divergence from trend

## 🔍 Code Structure

```python
def hp_filter(src, lambd=100):
    """
    Implements Hodrick-Prescott filter
    
    Parameters:
    src (array-like): Input time series
    lambd (float): Smoothing parameter
    
    Returns:
    pd.Series: Trend component
    """
```

## ⚙️ Configuration Options

| Parameter | Description | Default |
|-----------|-------------|---------|
| stock_symbol | Stock ticker to analyze | 'AAPL' |
| lambda_value | HP filter smoothing | 35 |
| display_mode | Divergence display type | "Percentage" |

## 📁 Project Structure

```
stock-trend-analysis/
│
├── stock_analysis.py      # Main script
├── requirements.txt      # Dependencies
├── README.md            # Documentation
└── .gitignore          # Git ignore rules
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the GNU General Public License v3 (GPLv3) (GPLv3) - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [yfinance](https://github.com/ranaroussi/yfinance) for providing stock data access
- Hodrick-Prescott filter methodology for trend analysis

## 📧 Contact

Your Name - [akbay.yavuz@gmail.com](mailto:akbay.yavuz@gmail.com)

Project Link: [https://github.com/YavuzAkbay/hodrick-prescott-filter](https://github.com/YavuzAkbay/hodrick-prescott-filter)

---
⭐️ If you found this project helpful, please consider giving it a star!