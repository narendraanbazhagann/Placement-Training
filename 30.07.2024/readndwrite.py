import csv


data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
