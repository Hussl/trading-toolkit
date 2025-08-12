# Candlestick Visualization (mplfinance)

Quick script to plot candlesticks with moving averages using `yfinance` + `mplfinance`.

## Run
```bash
pip install -r requirements.txt
python plot_candles.py --ticker BTC-USD --start 2024-01-01 --end 2025-08-01 --ma 20 50
```

Outputs `chart.png` in the folder.
