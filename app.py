import csv

filename = "sales_data.csv"

total_sales = 0
total_profit = 0
total_quantity = 0

sales_by_region = {}

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        sales = int(row["Sales"])
        profit = int(row["Profit"])
        quantity = int(row["Quantity"])

        total_sales += sales
        total_profit += profit
        total_quantity += quantity

        region = row["Region"]

        if region in sales_by_region:
            sales_by_region[region] += sales
        else:
            sales_by_region[region] = sales

print("=" * 40)
print("SALES DATA ANALYSIS")
print("=" * 40)

print(f"Total Sales    : ₹{total_sales}")
print(f"Total Profit   : ₹{total_profit}")
print(f"Total Quantity : {total_quantity}")

print("\nSales by Region")

for region, sales in sales_by_region.items():
    print(region, ":", sales)