# Validation

This project was checked through Python tests, SQLite checks and a manual Power BI review.

## Python

The test suite checks:

- required source files
- missing values
- primary-key uniqueness
- numeric validity
- referential integrity
- sale-to-opportunity consistency
- customer-to-region consistency
- revenue arithmetic
- Power BI-ready data consistency

Result: **10/10 tests passed**.

Run with:

```bash
python -m pytest -q
```

## SQL

The schema, data-quality queries and business-analysis queries were executed against the repository data using SQLite. The documented quality checks returned zero violations.

## Power BI

The reviewed `.pbix` report is included in `dashboard/`. It contains three pages: Executive Snapshot, Pipeline, and Customers & Growth.

The five core Power BI-ready tables match their corresponding source tables in `data/raw/`. The date dimension covers the full sales date range: `2025-01-15` to `2026-10-08` for sales, with `dim_date` covering `2025-01-01` to `2026-10-31`.

## Data boundary

The dataset is synthetic. Its results are not historical Asta Innovations results and no confidential company or customer information is included.
