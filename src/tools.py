"""
Tools module for the AI Data Quality Inspector.

This module contains separate tools for reading CSV files,
checking missing values, detecting duplicates, inspecting data types,
detecting outliers, checking category consistency, and generating reports.
"""

import os
from typing import Any, Dict

import pandas as pd


def read_csv_file(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file and returns it as a pandas DataFrame.
    """
    if not file_path or not file_path.strip():
        raise ValueError("File path cannot be empty.")

    if not file_path.lower().endswith(".csv"):
        raise ValueError("Only CSV files are supported.")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        dataframe = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        raise ValueError("The CSV file is empty.") from None

    if dataframe.empty:
        raise ValueError("The CSV file does not contain any rows.")

    return dataframe


def get_dataset_overview(dataframe: pd.DataFrame) -> Dict[str, Any]:
    """
    Creates a basic overview of the dataset.
    """
    return {
        "rows": len(dataframe),
        "columns": len(dataframe.columns),
        "column_names": list(dataframe.columns),
        "data_types": dataframe.dtypes.astype(str).to_dict(),
    }


def check_missing_values(dataframe: pd.DataFrame) -> Dict[str, Any]:
    """
    Checks missing values in each column.
    """
    missing_counts = dataframe.isnull().sum()

    missing_columns = {
        column: int(count)
        for column, count in missing_counts.items()
        if count > 0
    }

    return {
        "total_missing_values": int(missing_counts.sum()),
        "columns_with_missing_values": missing_columns,
    }


def check_duplicate_rows(dataframe: pd.DataFrame) -> Dict[str, Any]:
    """
    Detects fully duplicated rows in the dataset.

    A row is considered duplicated only if all column values are the same
    as a previous row.
    """
    duplicate_rows = dataframe[dataframe.duplicated()]

    return {
        "total_duplicate_rows": int(len(duplicate_rows)),
        "duplicate_row_indexes": duplicate_rows.index.tolist(),
    }


def inspect_data_types(dataframe: pd.DataFrame) -> Dict[str, Any]:
    """
    Inspects and classifies column data types.

    Columns are classified as:
    - numeric
    - date-like
    - text

    Date-like columns are detected using a clear date format to avoid
    pandas date parsing warnings.
    """
    type_result = {}

    for column in dataframe.columns:
        series = dataframe[column].dropna()

        if series.empty:
            detected_type = "empty"
        elif pd.api.types.is_numeric_dtype(series):
            detected_type = "numeric"
        else:
            text_series = series.astype(str).str.strip()

            converted_dates = pd.to_datetime(
                text_series,
                errors="coerce",
                format="%Y-%m-%d",
            )

            valid_date_ratio = converted_dates.notna().mean()

            if valid_date_ratio >= 0.6:
                detected_type = "date-like"
            else:
                detected_type = "text"

        type_result[column] = detected_type

    return type_result


def detect_outliers(dataframe: pd.DataFrame) -> Dict[str, Any]:
    """
    Detects numeric outliers using the IQR method.
    """
    outlier_result = {}
    numeric_columns = dataframe.select_dtypes(include="number").columns

    for column in numeric_columns:
        column_values = dataframe[column].dropna()

        if column_values.empty:
            continue

        q1 = column_values.quantile(0.25)
        q3 = column_values.quantile(0.75)
        iqr = q3 - q1

        if iqr == 0:
            continue

        lower_limit = q1 - 1.5 * iqr
        upper_limit = q3 + 1.5 * iqr

        outliers = column_values[
            (column_values < lower_limit) |
            (column_values > upper_limit)
        ]

        if not outliers.empty:
            outlier_result[column] = {
                "count": int(len(outliers)),
                "values": outliers.tolist(),
            }

    return outlier_result


def check_category_consistency(dataframe: pd.DataFrame) -> Dict[str, Any]:
    """
    Checks inconsistent text categories caused by capitalization or spacing.

    Example:
    Female, female, FEMALE
    """
    consistency_result = {}

    for column in dataframe.columns:
        column_data = dataframe[column]

        if pd.api.types.is_numeric_dtype(column_data):
            continue

        values = column_data.dropna().astype(str)

        if values.empty:
            continue

        normalized_groups = {}

        for value in values.unique():
            normalized_value = value.strip().lower()
            normalized_groups.setdefault(normalized_value, set()).add(value)

        inconsistent_groups = {
            key: sorted(list(original_values))
            for key, original_values in normalized_groups.items()
            if len(original_values) > 1
        }

        if inconsistent_groups:
            consistency_result[column] = inconsistent_groups

    return consistency_result


def check_column_quality(dataframe: pd.DataFrame) -> Dict[str, Any]:
    """
    Checks empty columns and columns with many missing values.
    """
    empty_columns = []
    high_missing_columns = []

    for column in dataframe.columns:
        missing_ratio = dataframe[column].isnull().mean()

        if missing_ratio == 1:
            empty_columns.append(column)
        elif missing_ratio >= 0.5:
            high_missing_columns.append(column)

    return {
        "empty_columns": empty_columns,
        "high_missing_columns": high_missing_columns,
    }


def generate_report(results: Dict[str, Any]) -> str:
    """
    Generates a structured Markdown report from analysis results.
    """
    overview = results["overview"]
    missing = results["missing_values"]
    duplicates = results["duplicates"]
    data_types = results["data_types"]
    outliers = results["outliers"]
    categories = results["category_consistency"]
    column_quality = results["column_quality"]

    report = []

    report.append("# Data Quality Report")
    report.append("")

    report.append("## Dataset Overview")
    report.append(f"- Rows: {overview['rows']}")
    report.append(f"- Columns: {overview['columns']}")
    report.append(f"- Column names: {', '.join(overview['column_names'])}")
    report.append("")

    report.append("## Missing Values")
    if missing["total_missing_values"] == 0:
        report.append("- No missing values were found.")
    else:
        report.append(f"- Total missing values: {missing['total_missing_values']}")
        for column, count in missing["columns_with_missing_values"].items():
            report.append(f"- Column `{column}` has {count} missing value(s).")
    report.append("")

    report.append("## Duplicate Rows")
    if duplicates["total_duplicate_rows"] == 0:
        report.append("- No duplicate rows were found.")
    else:
        report.append(f"- Duplicate rows found: {duplicates['total_duplicate_rows']}")
        report.append(
            f"- Duplicate row indexes: {duplicates['duplicate_row_indexes']}"
        )
    report.append("")

    report.append("## Data Types")
    for column, detected_type in data_types.items():
        report.append(f"- `{column}`: {detected_type}")
    report.append("")

    report.append("## Outliers")
    if not outliers:
        report.append("- No numeric outliers were detected.")
    else:
        for column, details in outliers.items():
            report.append(
                f"- Column `{column}` has {details['count']} possible outlier(s): "
                f"{details['values']}"
            )
    report.append("")

    report.append("## Category Consistency")
    if not categories:
        report.append("- No inconsistent text categories were detected.")
    else:
        for column, groups in categories.items():
            report.append(f"- Column `{column}` has inconsistent categories:")
            for normalized_value, variants in groups.items():
                report.append(f"  - `{normalized_value}` appears as: {variants}")
    report.append("")

    report.append("## Column Quality")
    if not column_quality["empty_columns"] and not column_quality["high_missing_columns"]:
        report.append("- No empty or very low-quality columns were detected.")
    else:
        if column_quality["empty_columns"]:
            report.append(f"- Empty columns: {column_quality['empty_columns']}")
        if column_quality["high_missing_columns"]:
            report.append(
                f"- Columns with many missing values: "
                f"{column_quality['high_missing_columns']}"
            )
    report.append("")

    report.append("## Recommendations")
    report.append("- Review and handle missing values.")
    report.append("- Remove duplicate rows if they are not intentional.")
    report.append("- Check possible outliers in numeric columns.")
    report.append("- Standardize inconsistent text categories.")
    report.append("- Confirm that detected data types match the real meaning of each column.")

    return "\n".join(report)
