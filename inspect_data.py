
import pandas as pd
from pathlib import Path

# Folder containing your downloaded Parquet files
DATA_DIR = Path(".")

files = [
    "customers.parquet",
    "orders.parquet",
    "order_items.parquet",
    "products.parquet",
    "returns.parquet",
    "sessions.parquet",
    "support_tickets.parquet",
]

for filename in files:
    file_path = DATA_DIR / filename

    print("\n" + "=" * 60)
    print(f"FILE: {filename}")
    print("=" * 60)

    if not file_path.exists():
        print("File not found. Check its location.")
        continue

    try:
        df = pd.read_parquet(file_path)

        print(f"Rows: {len(df):,}")
        print(f"Columns: {len(df.columns)}")

        print("\nColumn names and data types:")
        print(df.dtypes)

        print("\nFirst 5 rows:")
        print(df.head().to_string(index=False))

        print("\nMissing values per column:")
        print(df.isnull().sum())

    except Exception as error:
        print(f"Error reading {filename}: {error}")
