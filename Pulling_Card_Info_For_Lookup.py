import csv

filename = open('Moxfield Selling List 4-21-2025.csv', 'r' )

file = csv.DictReader(filename)

name = []

for col in file:
    name.append(col['Name'])

#debug name line check
print ('Name:', name)