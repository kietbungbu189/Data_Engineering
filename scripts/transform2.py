import csv
from pathlib import Path

product = {}

products_dir = "../workspaces/Data_Engineering/kiet_data/products.csv"

with open(products_dir, mode="r") as file:
    data = file.read()
    rows = data.splitlines()
    for row in rows[1:]:
        if row.strip():
            columns = row.split(",")
            product_id = columns[0]
            price = float(columns[1])
            product[product_id] = price

total_revenue = 0

sales_dir = "../workspaces/Data-Engineering/kiet_data/sales.csv"

with open(sales_dir, mode="r") as file:
    data2 = file.read()
    rows2 = data2.splitlines()
    for row2 in rows2[1:]:
        if row2.strip():
            columns2 = row2.split(",")
            sales_id = columns2[0]
            quantity = int(columns2[1])
            revenue = product[sales_id]*quantity
            total_revenue +=revenue


