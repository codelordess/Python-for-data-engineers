import csv

with open('data.csv') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    print(f'Header: {header}')
    
    for row in csv_reader:
        print(row)