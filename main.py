import csv

data = []

with open(".\data\worldcities.csv", encoding="utf8") as file:
    reader = csv.DictReader(file, delimiter=",")
    for row in reader:
        data.append(row)

print(data)