# Data Dictionary

All records in `data/raw/` are synthetic. The geography uses Indian city and state names for realism; the records do not represent real customers.

| Table | Key | Important fields | Purpose |
|---|---|---|---|
| customers | `customer_id` | type, industry, city, state, region, acquisition_date | Customer master and segmentation |
| products | `product_id` | product_name, category, unit_price | Product catalogue and pricing |
| sales_reps | `sales_rep_id` | region, team | Sales ownership |
| opportunities | `opportunity_id` | customer, product, lead_source, date, expected_value, stage, status, sales_rep | Pipeline analysis |
| sales | `sale_id` | opportunity, date, product, customer, rep, quantity, unit_price, revenue | Completed-sales analysis |
| market_analysis | `market_segment` | estimated_market_size_crore, estimated_growth_rate_pct, competitor_count | Synthetic market-scenario context |

## Key relationships

- `customers.customer_id` -> `opportunities.customer_id` and `sales.customer_id`
- `products.product_id` -> `opportunities.product_id` and `sales.product_id`
- `sales_reps.sales_rep_id` -> `opportunities.sales_rep_id` and `sales.sales_rep_id`
- `opportunities.opportunity_id` -> `sales.opportunity_id`

`market_analysis` contains synthetic scenario inputs. It is not company research or confidential market data.
