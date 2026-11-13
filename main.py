# import csv

# with open("sales.csv", "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row)



# import csv

# with open("sales.csv", "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         product = row["product"]
#         quantity = int(row["quantity"])
#         unit_price = int(row["unit_price"])

#         total = quantity * unit_price

#         print("Product:", product)
#         print("Quantity:", quantity)
#         print("Unit price:", unit_price)
#         print("Total:", total)
#         print("--------------------")



# import csv

# total_revenue = 0
# total_quantity = 0

# with open("sales.csv", "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         product = row["product"]
#         quantity = int(row["quantity"])
#         unit_price = int(row["unit_price"])

#         total = quantity * unit_price

#         total_revenue += total
#         total_quantity += quantity

#         print("Product:", product)
#         print("Total:", total)
#         print("--------------------")

# print("Total quantity:", total_quantity)
# print("Total revenue:", total_revenue)



# import csv

# total_revenue = 0
# total_quantity = 0

# with open("sales.csv", "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)

#     with open("sales_report.csv", "w", newline="", encoding="utf-8") as report_file:
#         writer = csv.writer(report_file)

#         writer.writerow(["Product", "Quantity", "Unit Price", "Total"])

#         for row in reader:
#             product = row["product"]
#             quantity = int(row["quantity"])
#             unit_price = int(row["unit_price"])

#             total = quantity * unit_price

#             total_revenue += total
#             total_quantity += quantity

#             writer.writerow([product, quantity, unit_price, total])

#         writer.writerow([])
#         writer.writerow(["TOTAL", total_quantity, "", total_revenue])

# print("Report created successfully!")
# print("Total quantity:", total_quantity)
# print("Total revenue:", total_revenue)



import csv

total_revenue = 0
total_quantity = 0

highest_revenue = 0
best_product = ""

# with open("sales.csv", "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)

#     with open("sales_report.csv", "w", newline="", encoding="utf-8") as report_file:
#         writer = csv.writer(report_file)

#         writer.writerow(["Product", "Quantity", "Unit Price", "Total"])

#         for row in reader:
#             product = row["product"]
#             quantity = int(row["quantity"])
#             unit_price = int(row["unit_price"])

#             total = quantity * unit_price

#             total_revenue += total
#             total_quantity += quantity

#             if total > highest_revenue:
#                 highest_revenue = total
#                 best_product = product

#             writer.writerow([product, quantity, unit_price, total])

#         writer.writerow([])
#         writer.writerow(["TOTAL", total_quantity, "", total_revenue])
#         writer.writerow(["Best product", best_product])
#         writer.writerow(["Highest revenue", highest_revenue])

# print("Report created successfully!")
# print("Total quantity:", total_quantity)
# print("Total revenue:", total_revenue)
# print("Best selling product:", best_product)
# print("Highest revenue:", highest_revenue)



from processor import process_sales

process_sales("sales_test.csv", "report.csv")

print("Report created successfully!")

