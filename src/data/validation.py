import pandas as pd


def validate_dataframe(df, required_columns=None):
    required_columns = required_columns or []
    missing = [column for column in required_columns if column not in df.columns]
    return {"valid": not missing, "missing_columns": missing, "rows": len(df), "columns": list(df.columns)}


def prepare_dataframe(df):
    cleaned = df.copy()
    if "Entity" in cleaned.columns:
        cleaned["Entity"] = cleaned["Entity"].astype("string").str.strip()
    if "Year" in cleaned.columns:
        cleaned["Year"] = pd.to_numeric(cleaned["Year"], errors="coerce").astype("Int64")
    for column in cleaned.columns:
        if column not in {"Entity", "Code", "Year", "World region according to OWID"}:
            cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")
    return cleaned.drop_duplicates().reset_index(drop=True)


def dataset_audit(df):
    audit = {
        "rows": len(df),
        "columns": list(df.columns),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_percent": (df.isna().mean() * 100).round(2).to_dict(),
    }
    if "Year" in df.columns and df["Year"].notna().any():
        audit["year_range"] = (int(df["Year"].min()), int(df["Year"].max()))
    if "Entity" in df.columns:
        audit["entities"] = int(df["Entity"].nunique(dropna=True))
    return audit
