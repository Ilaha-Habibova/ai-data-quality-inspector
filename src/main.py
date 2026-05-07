"""
Main entry point for the AI Data Quality Inspector.

This file receives the CSV file path from the user,
starts the Data Quality Agent, and prints the generated report.
"""

from agent import DataQualityAgent


def main():
    """
    Starts the command-line application.
    """
    print("AI Data Quality Inspector for CSV Files")
    print("--------------------------------------")

    default_path = "data/dirty_sample.csv"

    file_path = input(
        f"Enter CSV file path or press Enter to use sample file ({default_path}): "
    ).strip()

    if not file_path:
        file_path = default_path

    agent = DataQualityAgent()

    try:
        report = agent.analyze(file_path)

        print()
        print(report)

        report_file = "data_quality_report.md"

        with open(report_file, "w", encoding="utf-8") as file:
            file.write(report)

        print()
        print(f"Report saved to: {report_file}")

    except Exception as error:
        print()
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
