import csv
import sys
from pathlib import Path
from statistics import mean


def summarize(path, column):
    values = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None or column not in reader.fieldnames:
            raise SystemExit(f"Column '{column}' not found. Have: {reader.fieldnames}")
        for row in reader:
            raw = (row.get(column) or "").strip()
            if raw:
                values.append(float(raw))
    if not values:
        raise SystemExit("No numeric values found.")
    return {"count": len(values), "min": min(values), "max": max(values), "mean": mean(values)}


def main():
    if len(sys.argv) != 3:
        print("Usage: python csv_summary.py <file.csv> <column>")
        sys.exit(1)
    stats = summarize(Path(sys.argv[1]), sys.argv[2])
    for k, v in stats.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
