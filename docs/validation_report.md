# Project Validation and Quality Checks

## Purpose

This document records the data validation, SQL analysis checks, and automated tests performed for the Automotive Business Growth and Sales Analytics project.

## What Was Validated

The project includes checks for:

- Required source files and missing values
- Primary-key uniqueness and referential integrity
- Valid numerical values and sales calculations
- Consistency between sales, opportunities, customers, and regions
- Consistency of Power BI-ready tables with source data
- Coverage of the sales date range by the date dimension
- SQL business-analysis queries and data-quality checks

## Validation Results

| Check | Result |
|---|---|
| Python test suite | 10 of 10 tests passed |
| SQL data-quality checks | 10 checks passed with zero reported violations |
| SQL business-analysis queries | 5 queries executed successfully |
| SQL runner database | In-memory SQLite database |

## Reproducing the Checks

Run these commands from the repository root.

Python tests:

```bash
python -m pytest -q
```

SQL analysis:

```bash
python scripts/run_sql_analysis.py
```

The SQL runner loads the project CSV files into an in-memory database, applies the SQL schema, executes the analysis queries, and checks data quality without creating a persistent database file.

## Data Integrity and Transparency

The dataset is synthetic and intended for portfolio demonstration. The reported metrics describe this dataset; they are not actual company performance figures. Market-analysis values are scenario inputs, not independently verified market research.

## Scope and Limitations

The results above summarize the project's data-quality checks and SQL validation results, documenting the checks performed on the datasets and analysis.
