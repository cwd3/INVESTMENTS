import pytest
import psycopg2
from stockdb.pipelines.daily_update import run_daily_update
from stockdb.config import settings

pytestmark = pytest.mark.usefixtures("db_conn")

# --- Fake loaders for mocking ---
def fake_fundamentals(ticker: str):
    return {
        "eps": 5.0,
        "pe_ratio": 20.0,
        "roe": 0.15,
        "dividend_yield": 0.01,
        "free_cash_flow": 1000000,
    }

def fake_technicals(ticker: str):
    return {
        "sma_200": 150.0,
        "rsi": 55.0,
        "obv": 123456,
        "macd": 1.2,
    }

# --- DB fixture ---
@pytest.fixture
def db_conn():
    conn = psycopg2.connect(
        dbname=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASS,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
    )
    yield conn
    conn.close()

# --- Parameterized test with monkeypatch ---
@pytest.mark.mocked
@pytest.mark.parametrize("ticker", ["AAPL", "MSFT", "GOOG"])
def test_daily_update_with_mocked_data(db_conn, monkeypatch, ticker):
    # Patch both loaders with fakes
    monkeypatch.setattr("stockdb.loaders.fundamentals.get_fundamentals", fake_fundamentals)
    monkeypatch.setattr("stockdb.loaders.technicals.get_technicals", fake_technicals)

    run_daily_update(ticker)

    cur = db_conn.cursor()

    # Check fundamentals row exists
    cur.execute("SELECT COUNT(*) FROM fundamentals WHERE ticker = %s;", (ticker,))
    assert cur.fetchone()[0] > 0, f"No fundamentals row inserted for {ticker}"

    # Check technicals row exists
    cur.execute("SELECT COUNT(*) FROM technicals WHERE ticker = %s;", (ticker,))
    assert cur.fetchone()[0] > 0, f"No technicals row inserted for {ticker}"

    cur.close()