"""
Synthetic data generator for the Smart Financial Market Analytics case study.

Generates three datasets so the notebook is fully self-contained and does not
depend on downloading an external Kaggle archive:

  1. stock_market.csv      - daily OHLCV + sector + shares outstanding, 10 tickers
  2. financial_news.csv    - headlines per ticker/day with a sentiment label
  3. historical_trading.csv- individual buy/sell transaction records

Run:  python generate_data.py
"""

import os
import numpy as np
import pandas as pd

np.random.seed(42)

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

TICKERS = {
    "AAPL": ("Technology", 180.0, 15_500_000_000),
    "MSFT": ("Technology", 330.0, 7_400_000_000),
    "GOOGL": ("Technology", 140.0, 12_600_000_000),
    "AMZN": ("Consumer Discretionary", 145.0, 10_300_000_000),
    "JPM": ("Financials", 155.0, 2_900_000_000),
    "BAC": ("Financials", 33.0, 7_900_000_000),
    "XOM": ("Energy", 105.0, 4_200_000_000),
    "CVX": ("Energy", 155.0, 1_900_000_000),
    "JNJ": ("Healthcare", 160.0, 2_600_000_000),
    "PFE": ("Healthcare", 29.0, 5_600_000_000),
}

START_DATE = "2023-01-01"
END_DATE = "2024-12-31"

POS_HEADLINES = [
    "{sym} beats quarterly earnings expectations",
    "{sym} announces new product launch to strong demand",
    "Analysts upgrade {sym} on strong revenue growth",
    "{sym} shares rally after positive guidance",
    "{sym} reports record profit margins this quarter",
]
NEG_HEADLINES = [
    "{sym} misses earnings estimates, shares fall",
    "{sym} faces regulatory scrutiny over practices",
    "Analysts downgrade {sym} citing weak outlook",
    "{sym} shares slide on supply chain concerns",
    "{sym} announces layoffs amid cost-cutting drive",
]
NEU_HEADLINES = [
    "{sym} to present at industry conference next week",
    "{sym} schedules quarterly earnings call",
    "{sym} board approves routine dividend payment",
    "{sym} completes previously announced share buyback",
    "Market watchers await {sym} earnings report",
]

SOURCES = ["Reuters", "Bloomberg", "CNBC", "MarketWatch", "Financial Times"]
EXCHANGES = ["NYSE", "NASDAQ"]


def generate_stock_market(dates):
    rows = []
    for sym, (sector, start_price, shares_out) in TICKERS.items():
        price = start_price
        for d in dates:
            drift = np.random.normal(0.0003, 0.018)
            price = max(1.0, price * (1 + drift))
            open_p = price * (1 + np.random.normal(0, 0.004))
            close_p = price * (1 + np.random.normal(0, 0.004))
            high_p = max(open_p, close_p) * (1 + abs(np.random.normal(0, 0.006)))
            low_p = min(open_p, close_p) * (1 - abs(np.random.normal(0, 0.006)))
            volume = int(np.random.lognormal(mean=15.5, sigma=0.5))
            # inject a handful of volume/price anomaly spikes for anomaly detection
            if np.random.rand() < 0.01:
                volume *= np.random.randint(5, 10)
            if np.random.rand() < 0.005:
                close_p *= np.random.choice([0.85, 1.15])
            rows.append(
                [
                    d.strftime("%Y-%m-%d"),
                    sym,
                    sector,
                    round(open_p, 2),
                    round(high_p, 2),
                    round(low_p, 2),
                    round(close_p, 2),
                    volume,
                    shares_out,
                ]
            )
            price = close_p
    df = pd.DataFrame(
        rows,
        columns=[
            "Date", "Symbol", "Sector", "Open", "High", "Low",
            "Close", "Volume", "SharesOutstanding",
        ],
    )
    return df


def generate_news(dates):
    rows = []
    news_id = 1
    for d in dates:
        # not every ticker has news every day
        for sym in TICKERS:
            if np.random.rand() < 0.12:
                label = np.random.choice(
                    ["Positive", "Negative", "Neutral"], p=[0.4, 0.3, 0.3]
                )
                template = np.random.choice(
                    {"Positive": POS_HEADLINES, "Negative": NEG_HEADLINES, "Neutral": NEU_HEADLINES}[label]
                )
                rows.append(
                    [
                        news_id,
                        d.strftime("%Y-%m-%d"),
                        sym,
                        template.format(sym=sym),
                        np.random.choice(SOURCES),
                        label,
                    ]
                )
                news_id += 1
    return pd.DataFrame(
        rows, columns=["NewsID", "Date", "Symbol", "Headline", "Source", "SentimentLabel"]
    )


def generate_trading(dates):
    rows = []
    txn_id = 1
    symbols = list(TICKERS.keys())
    for d in dates:
        n_txn = np.random.randint(20, 40)
        for _ in range(n_txn):
            sym = np.random.choice(symbols)
            side = np.random.choice(["BUY", "SELL"])
            qty = int(np.random.lognormal(mean=6, sigma=1))
            price = round(TICKERS[sym][1] * (1 + np.random.normal(0, 0.05)), 2)
            rows.append(
                [
                    txn_id,
                    d.strftime("%Y-%m-%d"),
                    sym,
                    f"T{np.random.randint(1000, 9999)}",
                    side,
                    max(qty, 1),
                    max(price, 0.5),
                    np.random.choice(EXCHANGES),
                ]
            )
            txn_id += 1
    return pd.DataFrame(
        rows,
        columns=[
            "TransactionID", "Date", "Symbol", "TraderID",
            "BuySell", "Quantity", "Price", "Exchange",
        ],
    )


def main():
    dates = pd.bdate_range(START_DATE, END_DATE)  # business days only
    stock_df = generate_stock_market(dates)
    news_df = generate_news(dates)
    trading_df = generate_trading(dates)

    stock_df.to_csv(os.path.join(OUT_DIR, "stock_market.csv"), index=False)
    news_df.to_csv(os.path.join(OUT_DIR, "financial_news.csv"), index=False)
    trading_df.to_csv(os.path.join(OUT_DIR, "historical_trading.csv"), index=False)

    print(f"stock_market.csv       : {len(stock_df):,} rows")
    print(f"financial_news.csv     : {len(news_df):,} rows")
    print(f"historical_trading.csv : {len(trading_df):,} rows")


if __name__ == "__main__":
    main()
