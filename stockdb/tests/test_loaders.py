from stockdb.loaders.fundamentals import get_fundamentals

def test_get_fundamentals_returns_dict():
    data = get_fundamentals("AAPL")
    assert isinstance(data, dict)
    assert "eps" in data
    assert "pe_ratio" in data