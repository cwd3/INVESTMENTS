import pytest
from stockdb.db.connection import get_connection
from stockdb.db import writers

@pytest.fixture
def db_conn():
    conn = get_connection()
    yield conn
    conn.close()

def test_insert_company(db_conn):
    writers.insert_company("TEST", "Test Corp", "Tech", "Software")
    cur = db_conn.cursor()
    cur.execute("SELECT name, sector FROM companies WHERE ticker = %s;", ("TEST",))
    row = cur.fetchone()
    assert row == ("Test Corp", "Tech")