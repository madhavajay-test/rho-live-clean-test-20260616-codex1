import csv, sys
from decimal import Decimal

total = Decimal("0")
with open(sys.argv[1], newline="") as f:
    for row in csv.DictReader(f):
        total += Decimal(row["price"])
print(f"{total:.2f}")
