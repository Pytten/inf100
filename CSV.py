
from pathlib import Path

table_sting = Path('people.csv').read_text(encoding= 'utf-8')

lines = table_sting.splitlines()
header_line = lines[0]
data_lines = lines[1:]
headers = header_line.split(',')
number_of_cols = len(headers)



table_dict = []
for line in data_lines:
    row_dict = {}

    cells = line.split(',')

    for i in range(number_of_cols):
        header = headers[i]
        value = cells[i]
        row_dict[header] = value
    table_dict.append(row_dict)

print(table_dict)


# People .csv

# Navn,Alder,Høyde
# Ola,20,1.80
# Kari,19,1.65
# Per,21,1.73
# Oda,20,1.74


from csv import DictReader
from io import StringIO

file_string = Path('people.csv').read_text(encoding='utf-8')
reader = DictReader(StringIO(file_string), delimiter = ',', quotechar = '"')

print(file_string)