import csv
import os
from datetime import datetime

def iter_months(start, end):
    year = start.year
    month = start.month
    while (year, month) <= (end.year, end.month):
        yield year, month
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1


def parse_month(value):
    # Expect YYYY-MM-01; fall back to any YYYY-MM-DD
    return datetime.strptime(value, "%Y-%m-%d")


def check_file(path):
    dates = []
    missing_values = []
    with open(path, newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if not header or len(header) < 1:
            raise ValueError("Missing header or date column")
        for row in reader:
            if not row or not row[0].strip():
                continue
            dt = parse_month(row[0].strip())
            dates.append(dt)
            value = row[1].strip() if len(row) > 1 and row[1] is not None else ""
            if value == "":
                missing_values.append((dt.year, dt.month))

    if not dates:
        return {
            "file": os.path.basename(path),
            "min": None,
            "max": None,
            "missing": [],
            "duplicates": [],
            "missing_values": [],
        }

    dates.sort()
    min_dt = dates[0]
    max_dt = dates[-1]

    seen = set()
    duplicates = []
    for dt in dates:
        key = (dt.year, dt.month)
        if key in seen:
            duplicates.append(key)
        seen.add(key)

    missing = []
    for year, month in iter_months(min_dt, max_dt):
        if (year, month) not in seen:
            missing.append((year, month))

    return {
        "file": os.path.basename(path),
        "min": min_dt,
        "max": max_dt,
        "missing": missing,
        "duplicates": duplicates,
        "missing_values": missing_values,
    }


def format_months(items):
    return [f"{y:04d}-{m:02d}" for y, m in items]


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    files = ["CPIAUCSL.csv", "FEDFUNDS.csv", "INDPRO.csv", "UNRATE.csv"]

    for name in files:
        path = os.path.join(base_dir, name)
        result = check_file(path)
        print(f"\n{result['file']}")
        if result["min"] is None:
            print("  No data rows found")
            continue
        print(
            f"  Range: {result['min'].strftime('%Y-%m')} to {result['max'].strftime('%Y-%m')}"
        )
        if result["missing"]:
            print("  Missing months:")
            for item in format_months(result["missing"]):
                print(f"    {item}")
        else:
            print("  Missing months: none")
        if result["duplicates"]:
            print("  Duplicate months:")
            for item in format_months(sorted(set(result["duplicates"]))):
                print(f"    {item}")
        else:
            print("  Duplicate months: none")
        if result["missing_values"]:
            print("  Missing values:")
            for item in format_months(sorted(set(result["missing_values"]))):
                print(f"    {item}")
        else:
            print("  Missing values: none")


if __name__ == "__main__":
    main()
