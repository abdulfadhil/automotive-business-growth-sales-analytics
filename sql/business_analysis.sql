-- Business questions

-- 1. Revenue by region
SELECT region, SUM(revenue) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;

-- 2. Revenue by product
SELECT p.product_name, p.category, SUM(s.revenue) AS total_revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_name, p.category
ORDER BY total_revenue DESC;

-- 3. Opportunity conversion rate
SELECT
    ROUND(
        100.0 * SUM(CASE WHEN status = 'Won' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS conversion_rate_pct
FROM opportunities;

-- 4. Pipeline value by stage
SELECT stage, SUM(expected_value) AS pipeline_value
FROM opportunities
WHERE status = 'Open'
GROUP BY stage
ORDER BY pipeline_value DESC;


-- 5. Market opportunity ranking
SELECT
    market_segment,
    estimated_market_size_crore,
    estimated_growth_rate_pct,
    primary_competitor_count
FROM market_analysis
ORDER BY estimated_growth_rate_pct DESC, estimated_market_size_crore DESC;
