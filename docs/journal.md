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

---

# Step 2 — 08.05

## 1. Updated Description of the System Based on Implementation Progress

During Step 2, the system was developed from a planned concept into a first working prototype. The project now includes a command-line Python application that can receive a CSV file path from the user, load the dataset, analyze several data quality aspects, and generate a structured Markdown report.

The current prototype can analyze:

- dataset size and column names,
- missing values,
- duplicate rows,
- column data types,
- numeric outliers,
- inconsistent text categories,
- empty or low-quality columns.

The system uses a central Data Quality Agent that coordinates several specialized tools. Each tool performs one specific data quality task, and the agent combines all results into one final report.

At this stage, the project already demonstrates the main planned workflow:

```text
User provides CSV file path
        ↓
CSV Reader Tool loads the dataset
        ↓
Data Quality Agent coordinates analysis
        ↓
Specialized tools inspect data quality
        ↓
Report Generator Tool creates a Markdown report
        ↓
User receives the final report
```

The implementation is still a prototype, but the core structure of the system is already functional.

---

## 2. Refined List of Programming Concepts Actually Used

The following programming concepts have been actually used in the project during implementation:

| Programming Concept | Used In Project? | Where It Is Used |
|---|---|---|
| Python functions | Yes | Tools in `src/tools.py` |
| Modular programming | Yes | Separate files: `main.py`, `agent.py`, `tools.py` |
| Classes | Yes | `DataQualityAgent` class in `src/agent.py` |
| File handling | Yes | Reading CSV files and saving report files |
| pandas DataFrames | Yes | Loading and analyzing CSV datasets |
| Lists | Yes | Storing column names, outlier values, report lines |
| Dictionaries | Yes | Storing analysis results from tools |
| Loops | Yes | Processing columns and category values |
| Conditionals | Yes | Checking whether problems exist before reporting them |
| Error handling | Yes | Handling missing files, empty paths, invalid file types, and empty CSV files |
| Type hints | Yes | Function parameters and return values |
| Unit testing | Partially | Initial tests added in `tests/test_tools.py` |
| Git and GitHub | Yes | Repository commits show project progress |
| Markdown documentation | Yes | README and journal files |

---

## 3. Explanation of How Programming Concepts Are Applied in the Project

### Python Functions

Python functions are used to implement the individual tools of the system. For example, the missing value checker, duplicate row checker, outlier detector, category consistency checker, and report generator are all implemented as separate functions in `src/tools.py`.

This makes the system easier to understand, test, and extend.

### Modular Programming

The project is divided into separate modules:

- `src/main.py` starts the program and handles user interaction.
- `src/agent.py` contains the Data Quality Agent.
- `src/tools.py` contains the data quality inspection tools.
- `tests/test_tools.py` contains initial tests.

This structure keeps the code organized and separates responsibilities.

### Classes

The project uses a class called `DataQualityAgent`. This class represents the central agent of the system. It receives the CSV file path, calls all required tools, collects the results, and returns the final report.

### File Handling

File handling is used in two ways:

1. The system reads CSV files provided by the user.
2. The system saves the generated report as a Markdown file called `data_quality_report.md`.

### pandas DataFrames

The project uses pandas DataFrames to store and analyze CSV data. pandas makes it possible to count missing values, detect duplicate rows, inspect column types, and calculate numeric outliers.

### Lists and Dictionaries

Lists are used for column names, report lines, and detected outlier values.

Dictionaries are used to store structured results from each tool. For example, the missing value tool returns a dictionary containing the total number of missing values and the columns where missing values were found.

### Loops and Conditionals

Loops are used to analyze each column in the dataset.

Conditionals are used to check whether a problem exists. For example, the report generator checks whether missing values or duplicate rows were found before adding warning messages to the report.

### Error Handling

Error handling is used in the CSV Reader Tool. The system checks whether the file path is empty, whether the file exists, whether the file is a CSV file, and whether the CSV file contains data.

This prevents the program from crashing when invalid input is provided.

### Unit Testing

Initial unit tests were added using pytest. These tests check whether the main tools correctly detect missing values, duplicate rows, data types, outliers, and inconsistent categories.

---

## 4. Description of How Tools Are Integrated Into the System

The tools are integrated through the central Data Quality Agent.

The integration works as follows:

1. The user starts the program from `src/main.py`.
2. The program asks the user to provide a CSV file path.
3. `main.py` creates an object of the `DataQualityAgent` class.
4. The agent calls the CSV Reader Tool to load the dataset.
5. After the dataset is loaded, the agent calls each inspection tool.
6. Each tool returns structured results as dictionaries.
7. The agent passes all collected results to the Report Generator Tool.
8. The final Markdown report is returned to the user and saved as a file.

The integrated tools are:

| Tool | Integration Description |
|---|---|
| CSV Reader Tool | Called first by the agent to load the CSV file into a pandas DataFrame. |
| Dataset Overview Tool | Called after loading to collect basic dataset information. |
| Missing Value Tool | Receives the DataFrame and returns missing value statistics. |
| Duplicate Checker Tool | Receives the DataFrame and returns duplicate row information. |
| Data Type Inspector Tool | Receives the DataFrame and classifies column types. |
| Outlier Detection Tool | Receives numeric columns and detects unusual values using the IQR method. |
| Category Consistency Tool | Receives text columns and checks inconsistent capitalization or spelling. |
| Column Quality Tool | Checks whether columns are empty or contain many missing values. |
| Report Generator Tool | Receives all results and creates a structured Markdown report. |

This tool integration shows that the system is not a single simple script. It is an agent-based workflow where a central component coordinates several specialized tools to solve a practical data quality problem.

---

## Step 2 Progress Summary

In Step 2, the project was updated from a planned idea into a first working prototype. The system now contains implemented tools, an agent that coordinates them, a command-line entry point, initial tests, and updated documentation. The next step will focus on deeper testing, more test scenarios, deployment preparation, and explaining data conversion.
