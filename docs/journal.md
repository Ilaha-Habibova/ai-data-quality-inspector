# Project Journal

# Step 1 - 24.04

## Project Title

AI Data Quality Inspector for CSV Files

---

## 1. Short Description of the Planned System and Its Goal

The planned system is a Python-based AI-assisted data quality inspector for CSV files. The system will receive a CSV file from the user, analyze the dataset, detect common data quality problems, and generate a structured report.

The system will check problems such as:

- missing values,
- duplicate rows,
- possible wrong data types,
- invalid or suspicious values,
- numeric outliers,
- inconsistent text categories,
- empty or low-quality columns.

The main goal of the system is to help users quickly understand whether a dataset is clean, reliable, and ready for further use in data analysis, reporting, dashboards, or machine learning.

This system is useful because poor data quality can lead to incorrect conclusions. The tool will support students, analysts, and developers by automatically finding problems in CSV files and suggesting possible cleaning actions.

---

## 2. Description of the AI or Agent-Based Approach

The system will use an agent-based workflow. A central agent called the Data Quality Agent will coordinate several tools during execution.

The user will provide the path to a CSV file. The Data Quality Agent will then call different tools step by step. Each tool will perform a specific task, such as reading the file, checking missing values, detecting duplicates, analyzing data types, or finding outliers.

The agent will collect the results from all tools and generate a final report for the user.

The planned workflow is:

```text
User provides CSV file path
        ↓
CSV Reader Tool loads the dataset
        ↓
Data Quality Agent coordinates analysis
        ↓
Inspection tools check data problems
        ↓
Report Generator Tool creates final report
        ↓
User receives data quality report
```

The system can be considered AI-assisted because it does not only display raw statistics. It interprets detected problems, organizes them into understandable categories, and provides recommendations for improving the dataset.

---

## 3. List of Tools That Will Be Used in the System

The system will use several tools. Each tool will have a clear responsibility.

| Tool | Purpose |
|---|---|
| CSV Reader Tool | Reads the CSV file and converts it into a pandas DataFrame. |
| Missing Value Tool | Detects missing values in each column and calculates how many values are missing. |
| Duplicate Checker Tool | Finds repeated rows in the dataset. |
| Data Type Inspector Tool | Identifies numeric, text, date-like, and mixed-type columns. |
| Outlier Detection Tool | Detects unusual numeric values using simple statistical rules. |
| Category Consistency Tool | Finds inconsistent text categories, such as different capitalization or spelling. |
| Column Quality Tool | Detects empty columns or columns with very little useful information. |
| Report Generator Tool | Creates a structured final report with problems, warnings, and suggested cleaning actions. |

These tools will be connected to the Data Quality Agent. The agent will control the workflow, call the tools, collect their results, and prepare the final output.

---

## 4. Preliminary List of Programming Concepts Required

The project will require the following programming concepts:

| Programming Concept | How It Will Be Used |
|---|---|
| Python functions | To implement individual tools such as the missing value checker, duplicate checker, and outlier detector. |
| Modular programming | To separate the project into files such as main.py, agent.py, and tools.py. |
| Classes | To create the main Data Quality Agent that controls the workflow. |
| File handling | To read CSV files from the user-provided file path. |
| pandas DataFrames | To load, process, and analyze CSV data. |
| Lists and dictionaries | To store detected issues, statistics, and report results. |
| Conditionals | To check whether data quality problems exist and decide what message to show. |
| Loops | To analyze each column in the dataset. |
| Error handling | To handle missing files, invalid file paths, empty CSV files, and incorrect input. |
| Input validation | To check whether the user provided a valid CSV file. |
| Unit testing | To test the main tools and verify that they work correctly. |
| Git and GitHub | To track project development and show progress through regular commits. |
| Documentation | To explain how the system works and how another user can run it. |
| Deployment preparation | To prepare requirements.txt, startup instructions, and a clear README file. |

---

## 5. Target Audience and User Role

The target audience of the system includes data analysts, data scientists, business intelligence professionals, students, and developers who regularly work with CSV datasets.

The primary user role is the Data Quality Inspector User. This user provides a CSV file, starts the analysis process, and reviews the generated data quality report.

The system is designed for individual data quality inspection. At this stage, no separate administrator role or multi-user access control is planned.

---

## 6. Typical User Scenario

A typical user scenario is:

1. The user has a CSV file that needs to be checked before analysis.
2. The user provides the file path to the system.
3. The CSV Reader Tool loads the dataset.
4. The Data Quality Agent coordinates the inspection tools.
5. The tools check missing values, duplicates, data types, outliers, and category consistency.
6. The Report Generator Tool creates a structured report.
7. The user reviews the report and decides how to clean or improve the dataset.
## Step 1 Progress Summary

In Step 1, the project idea was selected and described. The planned system goal, agent-based workflow, planned tools, and preliminary programming concepts were defined. The next step will be to start implementing the basic CSV reading and data quality checking functionality.
