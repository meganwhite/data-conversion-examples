#read superheroes.json
import json
from pprint import pprint
import csv

with open('superheroes.json') as f:
	data = json.load(f)

#select members
members = data['members']

#write header to csv
with open('members.csv', 'w') as f:
	writer = csv.writer(f)
	header = [
		'name',
		'age',
		'secretIdentity',
		'powers',
		'squadName',
		'homeTown',
		'formed',
		'secretBase',
		'active']
	writer.writerow(header)

#loop over the members
	for m in members:
		row = [
			m['name'],
			m['age'],
			m['secretIdentity'],
			', '.join(m['powers']),
			data['squadName'],
			data['formed'],
			data['secretBase'],
			data['active']
		]
		writer.writerow(row)

