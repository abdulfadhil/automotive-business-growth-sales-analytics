-- Synthetic dataset: Automotive Business Growth & Sales Analytics

CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_type VARCHAR(30) NOT NULL,
    industry VARCHAR(50) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    region VARCHAR(30) NOT NULL,
    acquisition_date DATE NOT NULL
);

CREATE TABLE products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    unit_price DECIMAL(14,2) NOT NULL
);

CREATE TABLE sales_reps (
    sales_rep_id VARCHAR(10) PRIMARY KEY,
    sales_rep_name VARCHAR(100) NOT NULL,
    region VARCHAR(30) NOT NULL,
    team VARCHAR(30) NOT NULL
);


CREATE TABLE market_analysis (
    market_segment VARCHAR(100) PRIMARY KEY,
    estimated_market_size_crore DECIMAL(14,2) NOT NULL,
    estimated_growth_rate_pct DECIMAL(6,2) NOT NULL,
    primary_competitor_count INT NOT NULL
);

CREATE TABLE opportunities (
    opportunity_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(10) NOT NULL,
    product_id VARCHAR(10) NOT NULL,
    lead_source VARCHAR(50) NOT NULL,
    opportunity_date DATE NOT NULL,
    expected_value DECIMAL(14,2) NOT NULL,
    stage VARCHAR(30) NOT NULL,
    status VARCHAR(20) NOT NULL,
    sales_rep_id VARCHAR(10) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (sales_rep_id) REFERENCES sales_reps(sales_rep_id)
);

CREATE TABLE sales (
    sale_id VARCHAR(10) PRIMARY KEY,
    opportunity_id VARCHAR(20) NOT NULL,
    sale_date DATE NOT NULL,
    product_id VARCHAR(10) NOT NULL,
    customer_id VARCHAR(10) NOT NULL,
    sales_rep_id VARCHAR(10) NOT NULL,
    region VARCHAR(30) NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(14,2) NOT NULL,
    revenue DECIMAL(16,2) NOT NULL,
    FOREIGN KEY (opportunity_id) REFERENCES opportunities(opportunity_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (sales_rep_id) REFERENCES sales_reps(sales_rep_id)
);
