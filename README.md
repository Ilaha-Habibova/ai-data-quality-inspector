# AI Data Quality Inspector for CSV Files

## Project Overview

AI Data Quality Inspector for CSV Files is a Python-based AI-assisted software system designed to analyze CSV datasets and detect common data quality problems.

The system will help users understand whether a dataset is clean, reliable, and ready for further use in data analysis, reporting, dashboards, or machine learning.

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

The project will use an agent-based workflow. A central Data Quality Agent will coordinate several tools. Each tool will perform a specific task, such as reading the CSV file, checking missing values, detecting duplicates, analyzing data types, or generating the final report.

Planned workflow:

1. User provides a CSV file path.
2. CSV Reader Tool loads the dataset.
3. Data Quality Agent coordinates the analysis.
4. Inspection tools check different data quality problems.
5. Report Generator Tool creates a structured final report.

## Planned Tools

- CSV Reader Tool
- Missing Value Tool
- Duplicate Checker Tool
- Data Type Inspector Tool
- Outlier Detection Tool
- Category Consistency Tool
- Column Quality Tool
- Report Generator Tool

## Technologies

- Python
- pandas
- pytest
- Git and GitHub

## Current Status

Step 1 completed: planned system description, goal, agent-based approach, planned tools, and preliminary programming concepts.
