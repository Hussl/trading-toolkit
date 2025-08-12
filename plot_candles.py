
import argparse, yfinance as yf, mplfinance as mpf

def main(ticker, start, end, ma):
    df = yf.download(ticker, start=start, end=end, progress=False)
    if df.empty:
        raise SystemExit("No data returned. Check ticker or internet connection.")
    style = mpf.make_mpf_style(base_mpf_style='classic', mavcolors=['#1F77B4','#FF7F0E'])
    mpf.plot(df, type='candle', mav=ma, volume=True, style=style, savefig='chart.png')
    print("Saved chart.png")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--ticker", default="BTC-USD")
    ap.add_argument("--start", default="2024-01-01")
    ap.add_argument("--end", default=None)
    ap.add_argument("--ma", nargs="+", type=int, default=[20,50])
    args = ap.parse_args()
    main(args.ticker, args.start, args.end, args.ma)
