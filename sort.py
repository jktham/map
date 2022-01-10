import csv
import json
import time

start_time = time.time()

data = []
sorted = []
cities = []

with open(r".\data\simplemaps\worldcities.csv", encoding="utf8") as file:
    reader = csv.DictReader(file, delimiter=",")
    for row in reader:
        data.append(row)
        
cities = [city["city_ascii"] for city in data]

for i in range(len(data)):
    if cities.count(data[i]["city_ascii"]) > 1:
        sorted.append(data[i])

sorted.sort(key=lambda city: (float(city["population"]) * -1) if city["population"] else 0)
sorted.sort(key=lambda city: city["city_ascii"])

with open(r".\data\sorted.json", "w") as file:
    json.dump(sorted, file)

print(f"{len(sorted)}/{len(data)}, {time.time() - start_time}")
