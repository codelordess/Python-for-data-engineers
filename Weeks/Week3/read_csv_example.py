import csv
from pathlib import Path

data_file = Path(__file__).resolve().parent / 'data.csv'

with data_file.open(newline='') as file:
    reader = csv.reader(file)
    header = next(reader)
    print(f'Header: {header}')

    for row in reader:
        print(row)
