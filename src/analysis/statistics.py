import numpy as np


def correlation(df, x, y, method="pearson"):
    values = df[[x, y]].dropna() if x in df and y in df else df.iloc[0:0]
    if len(values) < 3:
        return None, len(values)
    coefficient = values[x].corr(values[y], method=method)
    return (float(coefficient) if np.isfinite(coefficient) else None), len(values)


def percent_change(first, last):
    if first is None or first == 0 or last is None:
        return None
    return float((last - first) / abs(first) * 100)


def describe_series(series):
    values = series.dropna()
    if values.empty:
        return {}
    return {"minimum": float(values.min()), "maximum": float(values.max()), "mean": float(values.mean()), "count": int(values.count())}
