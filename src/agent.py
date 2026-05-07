"""
Agent module for the AI Data Quality Inspector.

The DataQualityAgent coordinates all tools used to inspect CSV files
and generate a final data quality report.
"""

from tools import (
    read_csv_file,
    get_dataset_overview,
    check_missing_values,
    check_duplicate_rows,
    inspect_data_types,
    detect_outliers,
    check_category_consistency,
    check_column_quality,
    generate_report,
)


class DataQualityAgent:
    """
    Coordinates the full data quality inspection workflow.

    The agent receives a CSV file path, calls the required tools,
    collects their results, and returns a final report.
    """

    def __init__(self):
        self.name = "Data Quality Agent"

    def analyze(self, file_path: str) -> str:
        """
        Runs the full data quality analysis process.
        """
        dataframe = read_csv_file(file_path)

        results = {
            "overview": get_dataset_overview(dataframe),
            "missing_values": check_missing_values(dataframe),
            "duplicates": check_duplicate_rows(dataframe),
            "data_types": inspect_data_types(dataframe),
            "outliers": detect_outliers(dataframe),
            "category_consistency": check_category_consistency(dataframe),
            "column_quality": check_column_quality(dataframe),
        }

        report = generate_report(results)
        return report
