from datetime import date
from stockdb.loaders.fundamentals import get_fundamentals
from stockdb.loaders.technicals import get_technicals
from stockdb.db.writers import insert_company, insert_fundamentals, insert_technicals
from stockdb.utils.logging import logger

def run_daily_update(ticker: str):
    logger.info(f"Updating {ticker}")

    # Fundamentals
    fundamentals = get_fundamentals(ticker)
    if fundamentals:
        insert_company(ticker, f"{ticker} Inc.", "Unknown", "Unknown")
        insert_fundamentals(
            ticker,
            date.today(),
            fundamentals.get("eps"),
            fundamentals.get("pe_ratio"),
            fundamentals.get("roe"),
            fundamentals.get("dividend_yield"),
            fundamentals.get("free_cash_flow"),
        )

    # Technicals
    technicals = get_technicals(ticker)
    if technicals:
        insert_technicals(
            ticker,
            date.today(),
            technicals["sma_200"],
            technicals["obv"],
            technicals["rsi"],
            technicals["macd"],
        )
