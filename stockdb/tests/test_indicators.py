import pandas as pd
from stockdb.transformers.indicators import fisher_transform

def test_fisher_transform_runs():
    series = pd.Series([100, 101, 102, 103, 104, 105, 106, 107, 108, 109])
    fisher = fisher_transform(series, period=5)
    assert len(fisher) == len(series)
    # At least some values should not be None
    assert fisher.notna().sum() > 0