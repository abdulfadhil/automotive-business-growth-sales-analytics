from pathlib import Path
import re
import sqlite3
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parent.parent

TABLES = (
    "customers",
    "products",
    "sales_reps",
    "market_analysis",
    "opportunities",
    "sales",
)


def sql_statements(path):
    """Split this project's SQL files into executable statements."""
    content = path.read_text(encoding="utf-8")
    content = re.sub(r"--.*?$", "", content, flags=re.MULTILINE)
    return [part.strip() for part in content.split(";") if part.strip()]


def build_database():
    """Create a fresh in-memory SQLite database and load the CSV data."""
    connection = sqlite3.connect(":memory:")
    connection.execute("PRAGMA foreign_keys = ON")

    try:
        schema_path = ROOT / "sql" / "schema.sql"
        connection.executescript(
            schema_path.read_text(encoding="utf-8")
        )

        for table in TABLES:
            csv_path = ROOT / "data" / "raw" / f"{table}.csv"
            if not csv_path.is_file():
                raise FileNotFoundError(f"Missing source CSV: {csv_path}")

            frame = pd.read_csv(csv_path)
            frame.to_sql(
                table,
                connection,
                if_exists="append",
                index=False,
            )
            print(f"Loaded {len(frame):,} rows into {table}")

        violations = connection.execute(
            "PRAGMA foreign_key_check"
        ).fetchall()

        if violations:
            raise ValueError(
                f"Foreign-key violations found: {violations[:10]}"
            )

        return connection

    except Exception:
        connection.close()
        raise


def main():
    connection = build_database()

    try:
        print("\n=== BUSINESS ANALYSIS ===")
        business_path = ROOT / "sql" / "business_analysis.sql"

        for index, statement in enumerate(
            sql_statements(business_path), start=1
        ):
            cursor = connection.execute(statement)
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

            print(f"\nQuery {index}:")
            print(" | ".join(columns))
            for row in rows:
                print(" | ".join(str(value) for value in row))

        print("\n=== DATA QUALITY CHECKS ===")
        quality_path = ROOT / "sql" / "data_quality.sql"
        failures = []

        for statement in sql_statements(quality_path):
            cursor = connection.execute(statement)
            result = cursor.fetchone()

            if not cursor.description or result is None:
                raise ValueError(
                    "A quality query did not return a result."
                )

            check_name = cursor.description[0][0]
            count = int(result[0])
            status = "PASS" if count == 0 else "FAIL"

            print(f"{status}: {check_name} = {count}")

            if count != 0:
                failures.append((check_name, count))

        if failures:
            print(f"\nFAILED: {len(failures)} quality check(s).")
            return 1

        print("\nPASS: All SQL data-quality checks returned zero.")
        return 0

    finally:
        connection.close()


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
