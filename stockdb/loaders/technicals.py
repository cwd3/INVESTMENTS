import yfinance as yf
import pandas as pd
import ta

def get_technicals(ticker: str):
    data = yf.download(ticker, period="6mo", interval="1d", auto_adjust=False)

    if data.empty:
        return None

    # Ensure Close is a flat Series
    close = data["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]  # take the first column if it's 2D

    volume = data["Volume"]
    if isinstance(volume, pd.DataFrame):
        volume = volume.iloc[:, 0]

    # Compute indicators
    sma_200 = ta.trend.sma_indicator(close, window=200).iloc[-1]
    rsi = ta.momentum.rsi(close, window=14).iloc[-1]
    obv = ta.volume.on_balance_volume(close, volume).iloc[-1]
    macd = ta.trend.MACD(close).macd().iloc[-1]

    return {
        "sma_200": float(sma_200) if pd.notna(sma_200) else None,
        "rsi": float(rsi) if pd.notna(rsi) else None,
        "obv": float(obv) if pd.notna(obv) else None,
        "macd": float(macd) if pd.notna(macd) else None,
    }