import json
import matplotlib as plt
import geopandas as gpd

with open(r".\data\result.json") as file:
    data = json.load(file)

print(data)