from pathlib import Path

#directory:
file_dir = "../workspaces/Data_Engineering/kiet_data/products2.csv"
script

#content:
csv_content = """product_id,price
P001,10.00
P002,25.00
P003,8.50
P004,15.00
"""

#open:
with open(file_dir, mode="w") as file:
    file.write(csv_content)

#log:
print(f"file created sucessfully at {file_dir}")





