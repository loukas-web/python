import csv

path = '/home/loukas/asimakis.csv'
path2 = '/home/loukas/asimakis2.csv'
with open(path, 'r') as file:
    data = list(csv.reader(file))

a = [[1, 1], [2, 2]]

with open(path, 'w') as file:
    writer = csv.writer(file)
    writer.writerows(a)
    
    