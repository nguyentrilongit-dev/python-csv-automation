def calculate_revenue(quantity, unit_price):
    return quantity * unit_price


def is_valid_row(row):
    product = row["product"].strip()
    quantity = row["quantity"].strip()
    unit_price = row["unit_price"].strip()

    return bool(product and quantity and unit_price)
def process_sales(input_file, output_file):
    import csv

    seen_rows = set()
    total_quantity = 0
    total_revenue = 0
    valid_count = 0
    duplicate_count = 0
    invalid_count = 0

    with open(input_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        with open(output_file, "w", newline="", encoding="utf-8") as report:
            writer = csv.writer(report)

            writer.writerow(["Product", "Quantity", "Unit Price", "Revenue"])

            for row in reader:
                if not is_valid_row(row):
                    invalid_count += 1
                    continue

                product = row["product"].strip()
                quantity = int(row["quantity"])
                unit_price = int(row["unit_price"])

                row_key = (product, quantity, unit_price)

                if row_key in seen_rows:
                    duplicate_count += 1
                    continue

                seen_rows.add(row_key)

                revenue = calculate_revenue(quantity, unit_price)

                total_quantity += quantity
                total_revenue += revenue
                valid_count += 1

                writer.writerow([product, quantity, unit_price, revenue])

            writer.writerow([])
            writer.writerow(["TOTAL QUANTITY", total_quantity])
            writer.writerow(["TOTAL REVENUE", total_revenue])
            writer.writerow(["VALID ROWS", valid_count])
            writer.writerow(["DUPLICATE ROWS", duplicate_count])
            writer.writerow(["INVALID ROWS", invalid_count])