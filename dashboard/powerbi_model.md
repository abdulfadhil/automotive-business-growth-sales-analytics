# Power BI Model

## Tables
- dim_date
- dim_customer
- dim_product
- dim_sales_rep
- fact_sales
- fact_opportunities

## Relationships
- dim_date[date] -> fact_sales[sale_date]
- dim_customer[customer_id] -> fact_sales[customer_id]
- dim_customer[customer_id] -> fact_opportunities[customer_id]
- dim_product[product_id] -> fact_sales[product_id]
- dim_product[product_id] -> fact_opportunities[product_id]
- dim_sales_rep[sales_rep_id] -> fact_sales[sales_rep_id]
- dim_sales_rep[sales_rep_id] -> fact_opportunities[sales_rep_id]

## Core measures
```DAX
Total Revenue = SUM(fact_sales[revenue])

Total Sales = COUNTROWS(fact_sales)

Total Opportunities = COUNTROWS(fact_opportunities)

Won Opportunities =
CALCULATE(
    COUNTROWS(fact_opportunities),
    fact_opportunities[status] = "Won"
)

Conversion % =
DIVIDE([Won Opportunities], [Total Opportunities], 0)

Open Pipeline Value =
CALCULATE(
    SUM(fact_opportunities[expected_value]),
    fact_opportunities[status] = "Open"
)

Average Sale Value =
DIVIDE([Total Revenue], [Total Sales], 0)
```

## Customer measures

- **Total Customers:** distinct customers with at least one sale
- **Repeat Customers:** customers with more than one sale
- **Average Customer Value:** total revenue divided by customers with sales

## Date coverage

`dim_date` covers the full `fact_sales[sale_date]` range.
