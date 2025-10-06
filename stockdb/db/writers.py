from stockdb.db.connection import get_connection

def insert_company(ticker, name, sector, industry):
    sql = """
    INSERT INTO companies (ticker, name, sector, industry)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (ticker) DO NOTHING;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (ticker, name, sector, industry))

            
def insert_technicals(ticker, date, sma_200, obv, rsi, macd):
    sql = """
    INSERT INTO technicals (ticker, date, sma_200, obv, rsi, macd)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (ticker, date, sma_200, obv, rsi, macd))

def insert_fundamentals(ticker, date, eps, pe_ratio, roe, dividend_yield, free_cash_flow):
    sql = """
    INSERT INTO fundamentals (ticker, date, eps, pe_ratio, roe, dividend_yield, free_cash_flow)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (ticker, date, eps, pe_ratio, roe, dividend_yield, free_cash_flow))