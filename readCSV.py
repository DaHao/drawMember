import csv
import sys

with open('D://PythonProject//drawMember//membersBig5.csv', 'rt', encoding='cp950') as f:
    r = csv.DictReader(f)
    for row in r:
        print(row['Name'], ' ', row['Group'])
