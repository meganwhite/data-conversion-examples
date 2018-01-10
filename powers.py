#This python script brought to you by Megan White and Jackson Wright
#read superheroes.json
import json
from pprint import pprint

with open('superheroes.json') as f:
    data = json.load(f)

#create blank list of powers
powers = []

#loop over members
members = data['members']
for member in members:
	#for each member, loop over powers
	member_powers = member['powers']
	for power in member_powers:
		#add that to our list of powers
		powers.append(power)

#get only unique elements
unique_powers = list(set(powers))

#print those unique elements
pprint(unique_powers)

