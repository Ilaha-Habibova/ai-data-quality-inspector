# AI Data Quality Inspector for CSV Files

## Project Overview

AI Data Quality Inspector for CSV Files is a Python-based AI-assisted software system designed to analyze CSV datasets and detect common data quality problems.

The system helps users quickly assess whether a dataset is clean, reliable, and ready for further use in data analysis, reporting, dashboards, or machine learning. It reduces manual data checking by automatically detecting common issues and generating a structured data quality report.

## System Purpose

The main purpose of the system is to support users who work with CSV datasets and need to evaluate data quality before using the data further.

Poor data quality can lead to incorrect reports, misleading analysis, and unreliable machine learning results. This system aims to identify problems early and provide clear recommendations for improving the dataset.

## Target Audience

The system is mainly intended for:

- data analysts,
- data scientists,
- business intelligence specialists,
- students working with datasets,
- developers preparing data for applications or reports.

## User Role

The primary user role is the **Data Quality Inspector User**.

This user can:

1. Provide a CSV file path.
2. Start the data quality inspection process.
3. View the generated data quality report.
4. Use the recommendations to improve the dataset.

The system is designed for individual data quality review, so no separate administrator or multi-user access roles are planned at this stage.

## Implemented Features

The current prototype can:

- read a CSV file,
- show dataset overview,
- detect missing values,
- detect duplicate rows,
- inspect column data types,
- detect numeric outliers,
- detect inconsistent text categories,
- detect empty or low-quality columns,
- generate a Markdown data quality report.

## Agent-Based Approach

The project uses an agent-based workflow. A central **Data Quality Agent** coordinates several specialized tools. Each tool performs one specific task, such as reading the CSV file, checking missing values, detecting duplicates, analyzing data types, detecting outliers, or generating the final report.

The Data Quality Agent collects the results from all tools, organizes them, and returns a final structured data quality report.

## Current Workflow

1. The user provides a CSV file path.
2. The CSV Reader Tool loads the dataset into a pandas DataFrame.
3. The Data Quality Agent calls the inspection tools.
4. Each tool analyzes a specific quality aspect.
5. The Report Generator Tool creates a Markdown report.
6. The report is printed in the terminal and saved as `data_quality_report.md`.

## Implemented Tools

| Tool | Purpose |
|---|---|
| CSV Reader Tool | Loads the CSV file into the system. |
| Dataset Overview Tool | Shows number of rows, columns, column names, and data types. |
| Missing Value Tool | Detects empty or missing values in each column. |
| Duplicate Checker Tool | Finds repeated rows in the dataset. |
| Data Type Inspector Tool | Identifies numeric, text, and date-like columns. |
| Outlier Detection Tool | Detects unusual numeric values using the IQR method. |
| Category Consistency Tool | Finds inconsistent text categories, such as different capitalization or spelling. |
| Column Quality Tool | Detects empty or low-quality columns. |
| Report Generator Tool | Creates the final structured data quality report. |

## Technologies

- Python
- pandas
- pytest
- Git
- GitHub

## Project Structure

```text
ai-data-quality-inspector/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── docs/
│   └── journal.md
│
├── data/
│   └── dirty_sample.csv
│
├── src/
│   ├── main.py
│   ├── agent.py
│   └── tools.py
│
└── tests/
    └── test_tools.py
```

## How to Run the Current Prototype

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the program from the project root folder:

```bash
python src/main.py
```

When the program asks for a CSV file path, press Enter to use the sample file:

```text
data/dirty_sample.csv
```

Run tests:

```bash
pytest
```

## Current Status

Step 2 completed: first working prototype implemented. The system can read a CSV file, call multiple inspection tools through the Data Quality Agent, and generate a structured Markdown report.
