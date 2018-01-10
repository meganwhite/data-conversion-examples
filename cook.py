import csv
import json

#read veggies.csv
with open('veggies.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

#write JSON
with open('veggies.json', 'w') as f:
    json.dump(rows, f, indent=2)

