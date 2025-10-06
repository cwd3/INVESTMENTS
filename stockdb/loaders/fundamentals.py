import yfinance as yf

def get_fundamentals(ticker: str):
    stock = yf.Ticker(ticker)

    info = stock.info or {}
    eps = info.get("trailingEps")
    pe_ratio = info.get("trailingPE")

    # Fallback: try financials if info is empty
    if eps is None:
        try:
            eps = stock.financials.loc["Diluted EPS"].iloc[0]
        except Exception:
            eps = None

    return {
        "eps": eps,
        "pe_ratio": pe_ratio,
        "roe": info.get("returnOnEquity"),
        "dividend_yield": info.get("dividendYield"),
        "free_cash_flow": info.get("freeCashflow"),
    }