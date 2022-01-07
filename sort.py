import csv
import json
import time

start_time = time.time()

data = []
cities = []
result = []

with open(r".\data\simplemaps\worldcities.csv", encoding="utf8") as file:
    reader = csv.DictReader(file, delimiter=",")
    for row in reader:
        data.append(row)

for i in range(len(data)):        
    cities.append(data[i]["city_ascii"])

for i in range(len(cities)):
    if cities.count(cities[i]) > 1:
        result.append(data[i])

result.sort(key=lambda city: (city["city_ascii"], city["population"] * -1))

with open(r".\data\result.json", "w") as file:
    json.dump(result, file)

print(time.time() - start_time)
