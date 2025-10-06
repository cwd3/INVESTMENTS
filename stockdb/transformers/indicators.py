import pandas as pd
import numpy as np   # add this

def fisher_transform(series: pd.Series, period: int = 9):
    """Compute Fisher Transform of a price series."""
    min_val = series.rolling(period).min()
    max_val = series.rolling(period).max()
    value = 2 * ((series - min_val) / (max_val - min_val) - 0.5)

    # Use numpy instead of pd.np
    fisher = 0.5 * pd.Series(value).apply(
        lambda x: np.log((1 + x) / (1 - x)) if x not in (1, -1, None, float("nan")) else 0
    )
    return fisher