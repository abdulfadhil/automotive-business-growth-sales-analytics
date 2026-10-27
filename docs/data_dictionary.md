# Data Dictionary

## Data boundary

All records in `data/raw/` are synthetic. Indian city and state names are used for realism, but the records do not represent real customers or actual company transactions.

## Source tables

| Table | Primary key | Purpose |
|---|---|---|
| `customers` | `customer_id` | Customer details, industry, location, type, and acquisition date. |
| `products` | `product_id` | Product names, categories, and unit prices. |
| `sales_reps` | `sales_rep_id` | Sales representative names, regions, and teams. |
| `opportunities` | `opportunity_id` | Potential business, including lead source, expected value, stage, status, and ownership. |
| `sales` | `sale_id` | Recorded sales, including quantity, unit price, revenue, region, and related opportunity. |
| `market_analysis` | `market_segment` | Synthetic market-scenario estimates for market size, growth, and competitor count. |

## Column reference

### `customers.csv`

| Column | Meaning |
|---|---|
| `customer_id` | Unique identifier for a synthetic customer. |
| `customer_name` | Synthetic customer name. |
| `customer_type` | Customer classification. |
| `industry` | Industry associated with the customer. |
| `city`, `state`, `region` | Customer geography. |
| `acquisition_date` | Date the customer was acquired in the synthetic dataset. |

### `products.csv`

| Column | Meaning |
|---|---|
| `product_id` | Unique product identifier. |
| `product_name` | Product name. |
| `category` | Product category. |
| `unit_price` | Listed unit price in the dataset's currency. |

### `sales_reps.csv`

| Column | Meaning |
|---|---|
| `sales_rep_id` | Unique sales representative identifier. |
| `sales_rep_name` | Synthetic representative name. |
| `region` | Region assigned to the representative. |
| `team` | Team assigned to the representative. |

### `opportunities.csv`

| Column | Meaning |
|---|---|
| `opportunity_id` | Unique opportunity identifier. |
| `customer_id` | Customer associated with the opportunity. |
| `product_id` | Product associated with the opportunity. |
| `lead_source` | Source through which the opportunity was generated. |
| `opportunity_date` | Date the opportunity was recorded. |
| `expected_value` | Estimated value of the opportunity in the dataset's currency. |
| `stage` | Current pipeline stage. |
| `status` | Opportunity status, such as open or won. |
| `sales_rep_id` | Representative responsible for the opportunity. |

### `sales.csv`

| Column | Meaning |
|---|---|
| `sale_id` | Unique sale identifier. |
| `opportunity_id` | Opportunity associated with the sale. |
| `sale_date` | Date the sale was recorded. |
| `product_id`, `customer_id`, `sales_rep_id` | Product, customer, and representative associated with the sale. |
| `region` | Region recorded for the sale; validated against the customer's region. |
| `unit_price` | Unit price recorded for the sale. |
| `quantity` | Number of units sold. |
| `revenue` | Recorded sale revenue; validated against quantity multiplied by unit price. |

### `market_analysis.csv`

| Column | Meaning |
|---|---|
| `market_segment` | Synthetic market segment identifier and label. |
| `estimated_market_size_crore` | Estimated market size, expressed in crore in the synthetic scenario. |
| `estimated_growth_rate_pct` | Estimated growth rate, expressed as a percentage. |
| `primary_competitor_count` | Competitor count used in the synthetic scenario. |

These market values are scenario inputs, not verified external market research.

## Power BI-ready tables

The files in `dashboard/powerbi_ready/` prepare the data for the report.

| Table | Purpose |
|---|---|
| `dim_customer` | Customer attributes for filtering and grouping. |
| `dim_date` | Calendar attributes, including year, quarter, month, week, and day. |
| `dim_product` | Product attributes for analysis. |
| `dim_sales_rep` | Sales representative and team attributes. |
| `fact_opportunities` | Opportunity records for pipeline and conversion analysis. |
| `fact_sales` | Sales records for revenue and sales analysis. |

The five prepared customer, product, representative, opportunity, and sales tables are checked against their corresponding source CSVs by the automated test suite. The date dimension is checked to ensure it covers the full sales date range.

## Key relationships

- `customers.customer_id` -> `opportunities.customer_id` and `sales.customer_id`
- `products.product_id` -> `opportunities.product_id` and `sales.product_id`
- `sales_reps.sales_rep_id` -> `opportunities.sales_rep_id` and `sales.sales_rep_id`
- `opportunities.opportunity_id` -> `sales.opportunity_id`

The Power BI model's documented relationships and measures are described in [`dashboard/powerbi_model.md`](../dashboard/powerbi_model.md).

## Interpretation notes

- All operational records are synthetic and must not be presented as actual company performance.
- Monetary figures use the dataset's currency conventions; market size is explicitly expressed in crore.
- Field descriptions explain the dataset's intended meaning. They do not establish that the synthetic values reflect real-world market conditions.
