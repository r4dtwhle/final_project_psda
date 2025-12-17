"""
Data Loader with CSV support and fallback to sample data
"""

import os
import pandas as pd
from data.drivers_data import get_drivers


def load_from_csv(csv_path):
    """
    Load drivers data from CSV file (Kaggle dataset)

    Expected CSV columns:
    - name or driverName
    - points
    - wins
    - team or constructorName
    - avgLapTime or average_lap_time
    """
    try:
        df = pd.read_csv(csv_path)

        # Column mapping (flexible)
        column_map = {
            "driverName": "name",
            "constructorName": "team",
            "average_lap_time": "avgLapTime",
        }

        # Rename columns if needed
        df.rename(columns=column_map, inplace=True)

        # Convert to list of dictionaries
        drivers = []
        for idx, row in df.iterrows():
            driver = {
                "id": idx + 1,
                "name": row.get("name", f"Driver {idx+1}"),
                "points": int(row.get("points", 0)),
                "wins": int(row.get("wins", 0)),
                "team": row.get("team", "Unknown"),
                "avgLapTime": float(row.get("avgLapTime", 90.0)),
            }
            drivers.append(driver)

        print(f"✅ Loaded {len(drivers)} drivers from CSV")
        return drivers

    except Exception as e:
        print(f"⚠️ Error loading CSV: {e}")
        print("📦 Using sample data instead")
        return get_drivers()


def load_drivers():
    """
    Smart loader: Try CSV first, fallback to sample data

    To use Kaggle data:
    1. Download CSV from Kaggle
    2. Save as: data/f1_data.csv
    3. Dashboard will auto-detect and load it!
    """

    # Check for CSV files
    possible_paths = [
        "data/f1_data.csv",
        "data/f1_drivers.csv",
        "data/f1_drivers_2021.csv",
        "data/drivers.csv",
    ]

    for csv_path in possible_paths:
        if os.path.exists(csv_path):
            print(f"📊 Found CSV: {csv_path}")
            return load_from_csv(csv_path)

    # Fallback to sample data
    print("📦 Using sample data (no CSV found)")
    return get_drivers()


def get_sample_drivers():
    """Alias for get_drivers from drivers_data"""
    return get_drivers()