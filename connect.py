import psycopg2

# Adjust these values to match your setup
DB_NAME = "stockdb"          # or "postgres" if you haven't created stockdb yet
DB_USER = "postgres"         # or your dedicated role, e.g. "stockuser"
DB_PASS = "XeVwRkbSPz!ZbJcJev#ZT6W"    # the password you set/reset
DB_HOST = "localhost"
DB_PORT = "5432"

def main():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()

    # Insert a company
    cur.execute("""
        INSERT INTO companies (ticker, name, sector, industry)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (ticker) DO NOTHING;
    """, ("AAPL", "Apple Inc.", "Technology", "Consumer Electronics"))

    # Insert a fundamentals row
    cur.execute("""
        INSERT INTO fundamentals (ticker, date, eps, pe_ratio, de_ratio, roe, dividend_yield, free_cash_flow, buffett_indicator)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, ("AAPL", "2025-10-05", 6.12, 28.5, 1.2, 0.18, 0.006, 92000000000, 1.55))

    # Query back
    cur.execute("SELECT ticker, eps, pe_ratio FROM fundamentals WHERE ticker = %s;", ("AAPL",))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
