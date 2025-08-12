# Signal Filtering Tool

Takes a CSV of raw trade signals and applies basic filters to reduce low-quality trades.
Useful when you receive many signals but only want to take the best 3 per day.

## Input CSV format
`signals.csv` with columns: `timestamp,ticker,side,confidence,rsi,atr_volatility`
- `confidence`: 0..1 (higher is better)
- `rsi`: 0..100 (avoid overbought/oversold extremes)
- `atr_volatility`: normalized 0..1 (avoid ultra low liquidity)

## Filters (default)
- confidence >= 0.65
- 40 <= rsi <= 60 (neutral-momentum zone)
- atr_volatility >= 0.2
- Keep top 3 per day by confidence

## Run
```bash
pip install -r requirements.txt
python filter_signals.py --input signals.csv --output filtered.csv
```
