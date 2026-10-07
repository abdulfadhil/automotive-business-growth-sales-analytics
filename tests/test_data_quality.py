import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"


def load(name: str) -> pd.DataFrame:
    return pd.read_csv(RAW / name)


def test_required_files_exist():
    for filename in [
        "customers.csv", "products.csv", "sales_reps.csv",
        "opportunities.csv", "sales.csv", "market_analysis.csv",
    ]:
        assert (RAW / filename).exists(), filename


def test_core_tables_have_no_missing_values():
    for filename in [
        "customers.csv", "products.csv", "sales_reps.csv",
        "opportunities.csv", "sales.csv", "market_analysis.csv",
    ]:
        df = load(filename)
        assert df.isna().sum().sum() == 0, filename


def test_primary_keys_are_unique():
    checks = [
        ("customers.csv", "customer_id"),
        ("products.csv", "product_id"),
        ("sales_reps.csv", "sales_rep_id"),
        ("opportunities.csv", "opportunity_id"),
        ("sales.csv", "sale_id"),
        ("market_analysis.csv", "market_segment"),
    ]
    for filename, key in checks:
        df = load(filename)
        assert df[key].is_unique, f"Duplicate {key} in {filename}"


def test_positive_sales_and_non_negative_revenue():
    sales = load("sales.csv")
    assert (sales["quantity"] > 0).all()
    assert (sales["unit_price"] >= 0).all()
    assert (sales["revenue"] >= 0).all()


def test_non_negative_opportunity_and_market_values():
    opportunities = load("opportunities.csv")
    market = load("market_analysis.csv")
    assert (opportunities["expected_value"] >= 0).all()
    assert (market["estimated_market_size_crore"] >= 0).all()
    assert (market["estimated_growth_rate_pct"] >= 0).all()
    assert (market["primary_competitor_count"] >= 0).all()


def test_referential_integrity():
    customers = set(load("customers.csv")["customer_id"])
    products = set(load("products.csv")["product_id"])
    reps = set(load("sales_reps.csv")["sales_rep_id"])
    opportunities = load("opportunities.csv")
    sales = load("sales.csv")

    assert set(opportunities["customer_id"]).issubset(customers)
    assert set(opportunities["product_id"]).issubset(products)
    assert set(opportunities["sales_rep_id"]).issubset(reps)
    assert set(sales["customer_id"]).issubset(customers)
    assert set(sales["product_id"]).issubset(products)
    assert set(sales["sales_rep_id"]).issubset(reps)
    assert set(sales["opportunity_id"]).issubset(set(opportunities["opportunity_id"]))


def test_sale_matches_source_opportunity():
    sales = load("sales.csv")
    opportunities = load("opportunities.csv")
    joined = sales.merge(opportunities, on="opportunity_id", suffixes=("_sale", "_opp"))
    assert (joined["product_id_sale"] == joined["product_id_opp"]).all()
    assert (joined["customer_id_sale"] == joined["customer_id_opp"]).all()
    assert (joined["sales_rep_id_sale"] == joined["sales_rep_id_opp"]).all()


def test_sales_region_matches_customer_region():
    sales = load("sales.csv")
    customers = load("customers.csv")
    joined = sales.merge(customers[["customer_id", "region"]], on="customer_id", suffixes=("_sale", "_customer"))
    assert (joined["region_sale"] == joined["region_customer"]).all()


def test_revenue_matches_quantity_times_unit_price_within_tolerance():
    sales = load("sales.csv")
    expected = sales["quantity"] * sales["unit_price"]
    assert (sales["revenue"] - expected).abs().max() < 0.01


def test_powerbi_ready_tables_match_source_data_and_cover_sales_dates():
    pairs = [
        ("customers.csv", "dashboard/powerbi_ready/dim_customer.csv"),
        ("products.csv", "dashboard/powerbi_ready/dim_product.csv"),
        ("sales_reps.csv", "dashboard/powerbi_ready/dim_sales_rep.csv"),
        ("opportunities.csv", "dashboard/powerbi_ready/fact_opportunities.csv"),
        ("sales.csv", "dashboard/powerbi_ready/fact_sales.csv"),
    ]
    for raw_name, pbi_name in pairs:
        raw_df = pd.read_csv(ROOT / "data" / "raw" / raw_name)
        pbi_df = pd.read_csv(ROOT / pbi_name)
        pd.testing.assert_frame_equal(raw_df, pbi_df, check_dtype=False, check_like=False)

    date_dim = pd.to_datetime(pd.read_csv(ROOT / "dashboard" / "powerbi_ready" / "dim_date.csv")["date"])
    sales_dates = pd.to_datetime(load("sales.csv")["sale_date"])
    assert date_dim.min() <= sales_dates.min()
    assert date_dim.max() >= sales_dates.max()
