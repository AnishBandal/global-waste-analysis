import json
from functools import lru_cache

import pandas as pd
import streamlit as st

from .registry import DATASET_REGISTRY, dataset_path
from .validation import dataset_audit, prepare_dataframe


@st.cache_data(show_spinner=False)
def load_dataset(key):
    if key not in DATASET_REGISTRY:
        return pd.DataFrame()
    path = dataset_path(key)
    if not path.exists():
        return pd.DataFrame()
    return prepare_dataframe(pd.read_csv(path))


@lru_cache(maxsize=None)
def load_metadata(key):
    if key not in DATASET_REGISTRY:
        return {}
    spec = DATASET_REGISTRY[key]
    path = dataset_path(key).with_suffix(".metadata.json")
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def audit_all_datasets():
    return {key: dataset_audit(load_dataset(key)) for key in DATASET_REGISTRY}
