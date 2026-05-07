"""
Tests for the AI Data Quality Inspector tools.
"""

import sys
from pathlib import Path

import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from tools import (
    check_missing_values,
    check_duplicate_rows,
    inspect_data_types,
    detect_outliers,
    check_category_consistency,
)


def test_check_missing_values():
    dataframe = pd.DataFrame({
        "name": ["Alice", "Bob", None],
        "age": [20, None, 22],
    })

    result = check_missing_values(dataframe)

    assert result["total_missing_values"] == 2
    assert result["columns_with_missing_values"]["name"] == 1
    assert result["columns_with_missing_values"]["age"] == 1


def test_check_duplicate_rows():
    dataframe = pd.DataFrame({
        "id": [1, 2, 1],
        "name": ["Alice", "Bob", "Alice"],
    })

    result = check_duplicate_rows(dataframe)

    assert result["total_duplicate_rows"] == 1


def test_inspect_data_types():
    dataframe = pd.DataFrame({
        "age": [20, 25, 30],
        "name": ["Alice", "Bob", "Charlie"],
        "join_date": ["2024-01-01", "2024-02-01", "wrong-date"],
    })

    result = inspect_data_types(dataframe)

    assert result["age"] == "numeric"
    assert result["name"] == "text"
    assert result["join_date"] == "date-like"


def test_detect_outliers():
    dataframe = pd.DataFrame({
        "salary": [1000, 1100, 1200, 50000],
    })

    result = detect_outliers(dataframe)

    assert "salary" in result
    assert result["salary"]["count"] == 1


def test_check_category_consistency():
    dataframe = pd.DataFrame({
        "gender": ["Female", "female", "FEMALE", "Male"],
    })

    result = check_category_consistency(dataframe)

    assert "gender" in result
    assert "female" in result["gender"]
