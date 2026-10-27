# Automotive Sales and Business Analytics

A business analytics project exploring automotive sales, revenue, customer activity, product performance, and sales opportunities using Python, SQL, and Power BI.

## About the Project

This project was completed during a one-month internship at Asta Innovations in June 2024. It explores how business data can help explain sales performance, identify patterns, and present useful business insights.

The project brings together customer, product, sales, sales opportunity, sales representative, and market-segment datasets. It includes data validation, SQL analysis, Python-based KPI calculations, and a Power BI report.

All datasets are synthetic and included in this repository for demonstration. The results do not represent actual Asta Innovations performance or confidential company records.

## Problem Statement

Businesses need reliable information to understand sales performance, customer activity, product revenue, and potential revenue from sales opportunities. Before this information can support decisions, the data needs to be checked, analysed, and presented clearly.

This project explores questions about regional revenue, product performance, opportunity conversion, open pipeline value, lead sources, and repeat customers.

## Solution

The project follows a structured analytics workflow:

- **Python and Pandas** are used to inspect datasets, validate data, and calculate key metrics.
- **SQL and SQLite** are used to query the data and analyse business performance.
- **Data-quality checks** help identify invalid values and inconsistent relationships.
- **Power BI** presents the prepared data through business reporting pages.
- **Automated tests and documentation** help make the analysis easier to reproduce and review.

Together, these steps turn the supplied datasets into business metrics and findings that are easier to understand.

## Objectives and Features

- Explore revenue by region and product.
- Analyse sales opportunities, conversion rates, and open pipeline value.
- Examine customer activity and repeat purchasing.
- Validate data quality, keys, relationships, and numerical consistency.
- Prepare structured datasets for Power BI.
- Present key metrics and findings in a business intelligence report.
- Provide repeatable analysis scripts, automated tests, and documentation.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data analysis, calculations, and validation |
| Pandas | Working with structured datasets |
| SQL | Business queries and data-quality checks |
| SQLite | Executing SQL analysis against the CSV data |
| Power BI | Business reporting and dashboard visualisation |
| Jupyter Notebook | Exploring and documenting the analysis |
| pytest | Automated testing |
| Git | Version control |
| GitHub | Hosting and sharing the project |

## Datasets

The repository contains six synthetic datasets:

| Dataset | Records | Purpose |
|---|---:|---|
| Customers | 500 | Customer activity and purchasing analysis |
| Products | 15 | Product-level revenue analysis |
| Sales representatives | 20 | Sales representative information |
| Opportunities | 2,000 | Opportunity stages, outcomes, and conversion |
| Sales | 1,000 | Sales transactions and revenue |
| Market analysis | 5 | Illustrative market-segment scenarios |

The original CSV files are in `data/raw/`. Prepared datasets for Power BI are in `dashboard/powerbi_ready/`.

The datasets are provided with the project. They are not actual company records. The market-segment values are illustrative scenario inputs, not verified external market research.

## Key Results

The analysis produces the following results from the supplied synthetic data:

| Metric | Result |
|---|---:|
| Total revenue | ₹2,839,260,000 |
| Sales records | 1,000 |
| Total opportunities | 2,000 |
| Won opportunities | 444 |
| Opportunity conversion rate | 22.20% |
| Open pipeline value | ₹2,797,135,758 |
| Total customers | 500 |
| Customers with sales | 271 |
| Repeat customers | 218 |
| Average customer value | ₹10,476,974 |

### Selected Findings

- The South region contributes 27.33% of total revenue.
- EcoHaul Pro contributes 17.47% of total revenue.
- The Partner lead source has the highest conversion rate in the dataset, at 25.47%.
- Of the 500 customers, 271 have at least one recorded sale and 218 are repeat customers.

These findings describe patterns in the synthetic dataset. They should not be treated as actual company performance, verified market trends, or forecasts.

## Methodology

1. **Load the data:** Read the source CSV datasets for analysis.
2. **Validate data quality:** Check structure, keys, values, relationships, and numerical consistency.
3. **Analyse business performance:** Use Python and SQL to calculate metrics and answer business questions.
4. **Prepare reporting data:** Use the prepared datasets in `dashboard/powerbi_ready/`.
5. **Present the results:** Explore the findings through the Power BI report.
6. **Check reproducibility:** Run automated tests and SQL data-quality checks.

## Power BI Report

The Power BI report covers three areas:

- **Executive Snapshot:** An overview of key business metrics.
- **Pipeline:** Opportunity stages, conversion, and open pipeline value.
- **Customers & Growth:** Customer activity and growth-related metrics.

The Power BI report was created manually in Power BI Desktop.

Open the report in Power BI Desktop:

[`dashboard/automotive-business-growth-sales-analytics.pbix`](dashboard/automotive-business-growth-sales-analytics.pbix)

### Screenshots

**Executive Snapshot**

![Executive Snapshot](screenshots/executive-snapshot.png)

**Sales Pipeline**

![Sales Pipeline](screenshots/pipeline.png)

**Customers and Growth**

![Customers and Growth](screenshots/customers-and-growth.png)

## Getting Started

### Requirements

- Python 3
- Git
- Power BI Desktop to open the `.pbix` report

### 1. Clone the repository

```bash
git clone https://github.com/abdulfadhil/automotive-sales-business-analytics.git
cd automotive-sales-business-analytics
```

### 2. Create a virtual environment

For Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Run the SQL analysis

```powershell
python scripts/run_sql_analysis.py
```

The script loads the CSV datasets into an in-memory SQLite database, executes five business-analysis queries, and runs ten data-quality checks. It does not modify the source CSV files or create a persistent database.

### 5. Run the Python tests

```powershell
python -m pytest -q
```

The recorded validation run passed all 10 tests. The SQL data-quality checks also reported zero violations in the recorded run. Run the commands above to verify the results in your environment.

### 6. Explore the notebook

Open `python/business_analysis.ipynb` in Jupyter Notebook or Visual Studio Code to review the data checks, KPI calculations, and analysis.

### 7. Open the Power BI report

Open `dashboard/automotive-business-growth-sales-analytics.pbix` in Power BI Desktop to explore the report.

## Repository Structure

```text
automotive-sales-business-analytics/
|-- dashboard/
|   |-- automotive-business-growth-sales-analytics.pbix
|   |-- powerbi_model.md
|   `-- powerbi_ready/
|-- data/
|   `-- raw/
|-- docs/
|   |-- data_dictionary.md
|   `-- validation_report.md
|-- python/
|   `-- business_analysis.ipynb
|-- reports/
|   `-- business_insights.md
|-- screenshots/
|-- scripts/
|   `-- run_sql_analysis.py
|-- sql/
|   |-- business_analysis.sql
|   |-- data_quality.sql
|   `-- schema.sql
|-- tests/
|   `-- test_data_quality.py
|-- requirements.txt
|-- LICENSE
`-- README.md
```

## Project Documentation

- [Data Dictionary](docs/data_dictionary.md): Dataset descriptions, fields, keys, and relationships.
- [Validation Report](docs/validation_report.md): Data-quality checks and recorded results.
- [Power BI Data Model](dashboard/powerbi_model.md): Tables, relationships, and documented KPI calculations.
- [Business Insights](reports/business_insights.md): Summary of findings and limitations.
- [SQL Business Analysis](sql/business_analysis.sql): Queries used to analyse business performance.
- [SQL Data Quality Checks](sql/data_quality.sql): SQL validation rules.
- [Python Tests](tests/test_data_quality.py): Automated data-quality tests.

## Limitations

- The datasets are synthetic and do not represent actual company or customer records.
- Market-segment values are illustrative inputs, not verified external research.
- The findings demonstrate an analytics workflow and should not be interpreted as real-world business forecasts or performance claims.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for the terms.
