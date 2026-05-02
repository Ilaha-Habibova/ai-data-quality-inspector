# AI Data Quality Inspector for CSV Files

## Project Overview

AI Data Quality Inspector for CSV Files is a Python-based AI-assisted software system designed to analyze CSV datasets and detect common data quality problems.

The system helps users quickly assess whether a dataset is clean, reliable, and ready for further use in data analysis, reporting, dashboards, or machine learning. It reduces the need for manual data checking by automatically detecting common issues and generating a structured data quality report.

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

## Planned Features

The system is planned to detect:

- missing values,
- duplicate rows,
- possible wrong data types,
- invalid or suspicious values,
- numeric outliers,
- inconsistent text categories,
- empty or low-quality columns.

## Agent-Based Approach

The project will use an agent-based workflow. A central **Data Quality Agent** will coordinate several specialized tools. Each tool will perform one specific task, such as reading the CSV file, checking missing values, detecting duplicates, analyzing data types, or generating the final report.

The Data Quality Agent will collect the results from all tools, interpret the detected problems, and organize them into a clear final report.

## Planned Workflow

1. The user provides a CSV file path.
2. The CSV Reader Tool loads the dataset.
3. The Data Quality Agent coordinates the analysis.
4. Inspection tools check different data quality problems.
5. The Report Generator Tool creates a structured final report.
6. The user reviews the report and follows the suggested cleaning actions.

## Planned Tools

| Tool | Purpose |
|---|---|
| CSV Reader Tool | Loads the CSV file into the system. |
| Missing Value Tool | Detects empty or missing values in each column. |
| Duplicate Checker Tool | Finds repeated rows in the dataset. |
| Data Type Inspector Tool | Identifies numeric, text, date-like, and mixed-type columns. |
| Outlier Detection Tool | Detects unusual numeric values. |
| Category Consistency Tool | Finds inconsistent text categories, such as different capitalization or spelling. |
| Column Quality Tool | Detects empty or low-quality columns. |
| Report Generator Tool | Creates the final structured data quality report. |

## Technologies

The planned technologies are:

- Python,
- pandas,
- pytest,
- Git,
- GitHub.

## Data Handling

The system will process CSV files directly in memory using pandas DataFrames. The user data will not be permanently stored in a database during the first version of the project.

The generated report may be displayed in the terminal and later saved as a text or Markdown file.

## Current Status

Step 1 completed: planned system description, system goal, target audience, agent-based approach, planned tools, and preliminary programming concepts.
