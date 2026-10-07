# Automotive Business Growth & Sales Analytics

> A business analytics case study based on work handled during a June 2024 Business Analytics internship at Asta Innovations, Chennai.

## Context

During the internship, my work covered business and market research, competitor analysis, business development, client communication, opportunity assessment, SQL, Excel and Power BI. I was also involved in closing **10+ business opportunities**.

The public dataset is **synthetic**. It does not contain Asta Innovations' internal database, customer records or confidential operational data.

## The problem

An early-stage automotive business can have customer, sales, product and opportunity information spread across different records.

The aim is a clear view of revenue, pipeline and customer activity for business and sales decisions.

The analysis is built to answer practical questions:

- Which products generate more revenue?
- Which regions perform better?
- How large is the open pipeline?
- Which lead sources convert better?
- Which customer segments need attention?

## The solution

```text
Synthetic Data
   -> Validation
   -> SQL
   -> Python / Pandas
   -> Power BI
   -> Business Insights
```

## Dataset

All operational records are synthetic.

| Table | Records | Purpose |
|---|---:|---|
| Customers | 500 | Customer, industry and geography |
| Products | 15 | Product and pricing information |
| Sales Representatives | 20 | Sales ownership and region |
| Opportunities | 2,000 | Pipeline and conversion analysis |
| Sales | 1,000 | Revenue analysis |
| Market Analysis | 5 | Synthetic market-scenario context |

The geography uses Indian city and state names only to keep the sample realistic. The records do not represent real customers.

## Key results

These figures come only from the synthetic dataset:

| KPI | Result |
|---|---:|
| Revenue | ₹2,839,260,000 |
| Sales | 1,000 |
| Opportunities | 2,000 |
| Won Opportunities | 444 |
| Conversion Rate | 22.20% |
| Open Pipeline | ₹2,797,135,758 |
| Customers with Sales | 271 |
| Repeat Customers | 218 |
| Average Customer Value | ₹10,476,974 |

A few notable patterns:

- **Top region:** South — 27.33% of revenue
- **Top product:** EcoHaul Pro — 17.47% of revenue
- **Best lead source by conversion:** Partner — 25.47%

These are descriptive findings from synthetic data, not company performance.

## Power BI

The report has three pages:

- **Executive Snapshot** — revenue, sales, opportunities, conversion and performance
- **Pipeline** — opportunity status, pipeline by stage and lead-source conversion
- **Customers & Growth** — customer type, industry, region and customer metrics

The reviewed `.pbix` file is included in `dashboard/`.

The six files in `dashboard/powerbi_ready/` are the report's import-ready tables.

## Validation

The repository includes automated checks for missing values, primary-key uniqueness, numeric validity, referential integrity, sale-to-opportunity consistency, customer-to-region consistency and revenue arithmetic.

The Python test suite passes **10/10 tests**. SQL quality checks and business queries were also executed against the repository data.

## Structure

```text
data/raw/              -> synthetic source data
sql/                    -> schema, quality checks and analysis queries
python/                 -> reproducible analysis notebook
dashboard/              -> Power BI report and model
docs/                   -> data reference and validation
reports/                -> business insights
tests/                  -> automated data-quality tests
```

## Run

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
# source .venv/bin/activate

python -m pip install -r requirements.txt
python -m pytest -q
```

Main analysis notebook:

```text
python/business_analysis.ipynb
```

SQL files can be run against SQLite or another compatible relational database.

## Boundaries

- The operational dataset is synthetic.
- Synthetic results are not historical Asta Innovations results.
- No confidential company or customer information is included.
- This is an analytics case study, not a production sales system.
