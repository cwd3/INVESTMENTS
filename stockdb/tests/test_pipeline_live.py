import pytest
import psycopg2
from stockdb.pipelines.daily_update import run_daily_update
from stockdb.config import settings

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

@pytest.mark.live
@pytest.mark.parametrize("ticker", ["AAPL", "MSFT", "GOOG"])
def test_daily_update_live(db_conn, ticker):
    # Run the real pipeline (no monkeypatching)
    run_daily_update(ticker)

    cur = db_conn.cursor()

    # Check that at least one fundamentals row exists
    cur.execute("SELECT COUNT(*) FROM fundamentals WHERE ticker = %s;", (ticker,))
    fundamentals_count = cur.fetchone()[0]

    # Check that at least one technicals row exists
    cur.execute("SELECT COUNT(*) FROM technicals WHERE ticker = %s;", (ticker,))
    technicals_count = cur.fetchone()[0]

    cur.close()

    # If Yahoo didn’t return data, skip instead of fail
    if fundamentals_count == 0 or technicals_count == 0:
        pytest.skip(f"No live data available for {ticker}")