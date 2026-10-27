# Power BI Data Model

## Purpose

This document describes the tables, relationships, and core measures used for the Automotive Business Growth and Sales Analytics report.

## Report Pages

The report is organised around three business areas:

- **Executive Snapshot:** high-level business performance and KPIs.
- **Pipeline:** opportunity stages, conversion, and open pipeline value.
- **Customers & Growth:** customer activity and growth-related analysis.

## Tables

| Table | Purpose |
|---|---|
| `dim_date` | Calendar attributes for analysing sales over time |
| `dim_customer` | Customer details and segmentation |
| `dim_product` | Product names, categories, and prices |
| `dim_sales_rep` | Sales representative and team information |
| `fact_sales` | Recorded sales, quantities, and revenue |
| `fact_opportunities` | Sales opportunities, stages, status, and expected value |

## Relationships

The documented model connects the dimensions to the relevant fact tables:

| Dimension | Key | Fact table | Matching column |
|---|---|---|---|
| `dim_date` | `date` | `fact_sales` | `sale_date` |
| `dim_customer` | `customer_id` | `fact_sales` | `customer_id` |
| `dim_customer` | `customer_id` | `fact_opportunities` | `customer_id` |
| `dim_product` | `product_id` | `fact_sales` | `product_id` |
| `dim_product` | `product_id` | `fact_opportunities` | `product_id` |
| `dim_sales_rep` | `sales_rep_id` | `fact_sales` | `sales_rep_id` |
| `dim_sales_rep` | `sales_rep_id` | `fact_opportunities` | `sales_rep_id` |

## Core Measures

The following DAX expressions describe the documented KPI definitions.

### Total Revenue

```dax
Total Revenue = SUM(fact_sales[revenue])
```

### Total Sales

```dax
Total Sales = COUNTROWS(fact_sales)
```

This counts sales records, not the total quantity of products sold.

### Total Opportunities

```dax
Total Opportunities = COUNTROWS(fact_opportunities)
```

### Won Opportunities

```dax
Won Opportunities =
CALCULATE(
    COUNTROWS(fact_opportunities),
    fact_opportunities[status] = "Won"
)
```

### Conversion Rate

```dax
Conversion % =
DIVIDE(
    [Won Opportunities],
    [Total Opportunities],
    0
)
```

Format this measure as a percentage in Power BI.

### Open Pipeline Value

```dax
Open Pipeline Value =
CALCULATE(
    SUM(fact_opportunities[expected_value]),
    fact_opportunities[status] = "Open"
)
```

### Average Sale Value

```dax
Average Sale Value =
DIVIDE(
    [Total Revenue],
    [Total Sales],
    0
)
```

This represents average revenue per sales record.

## Customer Measures

- **Customers with Sales:** distinct customers with at least one recorded sale.
- **Repeat Customers:** customers with more than one recorded sale.
- **Average Customer Value:** total revenue divided by the number of distinct customers with sales.

These definitions describe the intended calculations. The exact DAX expressions and filter behaviour should be checked against the Power BI file before being treated as a verified implementation.

## Date Coverage

The prepared date dimension is documented as covering `2025-01-01` through `2026-10-31`. The sales dates range from `2025-01-15` through `2026-10-08`.

## Implementation Note

This document describes the intended data model and KPI definitions. It is not, by itself, proof that every relationship, measure, visual, or interaction has been verified in Power BI Desktop.
