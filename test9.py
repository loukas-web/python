import csv

path = '/home/loukas/asimakis.csv'

with open(path) as file:
    data = list(csv.reader(file))

print(data)

for d in data:
    print(d)
