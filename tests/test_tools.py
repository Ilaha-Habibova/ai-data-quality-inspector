"""
Tests for the AI Data Quality Inspector tools.
"""

import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from tools import (
    read_csv_file,
    check_missing_values,
    check_duplicate_rows,
    inspect_data_types,
    detect_outliers,
    check_category_consistency,
    check_column_quality,
)


def test_read_csv_file_valid_file(tmp_path):
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text("id,name\n1,Alice\n2,Bob\n", encoding="utf-8")

    dataframe = read_csv_file(str(csv_file))

    assert len(dataframe) == 2
    assert list(dataframe.columns) == ["id", "name"]


def test_read_csv_file_rejects_non_csv_file(tmp_path):
    text_file = tmp_path / "sample.txt"
    text_file.write_text("not a csv file", encoding="utf-8")

    with pytest.raises(ValueError):
        read_csv_file(str(text_file))


def test_check_missing_values():
    dataframe = pd.DataFrame({
        "name": ["Alice", "Bob", None],
        "age": [20, None, 22],
    })

    result = check_missing_values(dataframe)

    assert result["total_missing_values"] == 2
    assert result["columns_with_missing_values"]["name"] == 1
    assert result["columns_with_missing_values"]["age"] == 1


def test_check_exact_duplicate_rows():
    dataframe = pd.DataFrame({
        "id": [1, 2, 1],
        "name": ["Alice", "Bob", "Alice"],
        "age": [23, 30, 23],
    })

    result = check_duplicate_rows(dataframe)

    assert result["total_duplicate_rows"] == 1
    assert result["duplicate_row_indexes"] == [2]


def test_check_possible_duplicate_records_with_different_id():
    dataframe = pd.DataFrame({
        "id": [1, 6],
        "name": ["Alice", "Alice"],
        "age": [23, 23],
        "email": ["alice@example.com", "alice@example.com"],
    })

    result = check_duplicate_rows(dataframe)

    assert result["total_duplicate_rows"] == 0
    assert result["possible_duplicate_records"] == 1
    assert result["possible_duplicate_record_indexes"] == [1]
    assert result["ignored_identifier_columns"] == ["id"]


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


def test_check_column_quality():
    dataframe = pd.DataFrame({
        "full_column": [1, 2, 3, 4],
        "high_missing_column": [1, None, None, None],
        "empty_column": [None, None, None, None],
    })

    result = check_column_quality(dataframe)

    assert "empty_column" in result["empty_columns"]
    assert "high_missing_column" in result["high_missing_columns"]
