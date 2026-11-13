# Python CSV Automation

A Python project that validates and processes sales data from a CSV file, removes duplicate records, calculates revenue, and writes a summary report.

## Features

- Read sales data with Python's built-in `csv` module.
- Skip rows with missing fields.
- Ignore duplicate sales records.
- Calculate revenue and totals.
- Generate a CSV report.
- Test functions with `unittest`.

## Project Structure

```text
python-csv-automation/
├── main.py
├── processor.py
├── test_processor.py
├── sales_test.csv
├── report.csv
├── .gitignore
└── README.md
```

## Requirements

- Python 3.x

## Run the project

```bash
python main.py
```

The program reads `sales_test.csv` and creates `report.csv`.

## Run the tests

```bash
python test_processor.py
```

## Example results

Using the included sample data:

- Valid rows: 3
- Duplicate rows: 1
- Invalid rows: 1
- Total quantity: 6
- Total revenue: 3,650,000 VND

## Technologies

- Python
- CSV
- `unittest`

## Author

Computer Science Student
