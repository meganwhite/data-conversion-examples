vegetables = [
 {"name": "eggplant"},
 {"name": "tomato"},
 {"name": "corn"},
 {"name": "rutabega"},
 {"name": "squash"},
 {"name": "kale"},
 {"name": "pizza"},
 {"name": "tomato"},
 {"name": "tomato"},
 {"name": "tomato"},
]

print(vegetables)

import csv

with open('veggies.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'length'])
    for vegetable in vegetables:
    	#I want the name of the vegetable 
    	vegetable_name = vegetable['name']
    	#I want the length of the word
    	vegetable_name_length = len(vegetable['name'])
    	#Write to CSV
    	row = [vegetable_name,vegetable_name_length]
    	writer.writerow(row)

