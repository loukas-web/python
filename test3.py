import csv

with open("test.csv") as file:
    data = list(csv.reader(file))

# print(data)
c=[]
for i in range(len(data[0])):
    c.append([data[0][i], data[1][i]])

print(c)