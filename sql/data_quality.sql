-- Data quality checks for the synthetic dataset.

-- Missing customer keys in opportunities
SELECT COUNT(*) AS orphan_opportunity_customers
FROM opportunities o
LEFT JOIN customers c ON c.customer_id = o.customer_id
WHERE c.customer_id IS NULL;

-- Missing product keys in opportunities
SELECT COUNT(*) AS orphan_opportunity_products
FROM opportunities o
LEFT JOIN products p ON p.product_id = o.product_id
WHERE p.product_id IS NULL;

-- Missing sales-rep keys in opportunities
SELECT COUNT(*) AS orphan_opportunity_reps
FROM opportunities o
LEFT JOIN sales_reps r ON r.sales_rep_id = o.sales_rep_id
WHERE r.sales_rep_id IS NULL;

-- Missing customer keys in sales
SELECT COUNT(*) AS orphan_sale_customers
FROM sales s
LEFT JOIN customers c ON c.customer_id = s.customer_id
WHERE c.customer_id IS NULL;

-- Missing product keys in sales
SELECT COUNT(*) AS orphan_sale_products
FROM sales s
LEFT JOIN products p ON p.product_id = s.product_id
WHERE p.product_id IS NULL;

-- Missing sales-rep keys in sales
SELECT COUNT(*) AS orphan_sale_reps
FROM sales s
LEFT JOIN sales_reps r ON r.sales_rep_id = s.sales_rep_id
WHERE r.sales_rep_id IS NULL;

-- Sales should reference a real opportunity.
SELECT COUNT(*) AS orphan_sale_opportunities
FROM sales s
LEFT JOIN opportunities o ON o.opportunity_id = s.opportunity_id
WHERE o.opportunity_id IS NULL;

-- Basic numeric validity
SELECT COUNT(*) AS invalid_sales
FROM sales
WHERE quantity <= 0 OR unit_price < 0 OR revenue < 0;

SELECT COUNT(*) AS invalid_opportunities
FROM opportunities
WHERE expected_value < 0;

-- Market-analysis validity
SELECT COUNT(*) AS invalid_market_rows
FROM market_analysis
WHERE estimated_market_size_crore < 0
   OR estimated_growth_rate_pct < 0
   OR primary_competitor_count < 0;
