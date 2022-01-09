import json

import folium
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry.linestring import LineString

with open(r".\data\result.json") as file:
    data = json.load(file)

df = pd.DataFrame({
    "Name": [city["city_ascii"] for city in data],
    "Country": [city["country"] for city in data],
    "Population": [city["population"] for city in data],
    "Latitude": [city["lat"] for city in data],
    "Longitude": [city["lng"] for city in data]
})

geometry = []

for i in range(len(data)):
    j = 1
    if data[i]["city_ascii"] != data[i-1]["city_ascii"]:
        while data[i+j]["city_ascii"] == data[i]["city_ascii"]:
            geometry.append(LineString(coordinates=((float(data[i]["lng"]), float(data[i]["lat"])), (float(data[i+j]["lng"]), float(data[i+j]["lat"])))))
            j += 1
            if i+j == len(data):
                break

points = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
lines = gpd.GeoDataFrame(geometry=geometry)

background = folium.Map()
map = lines.explore(m=background, style_kwds=dict(weight=0.2, color="red"))
map = points.explore(m=map, marker_kwds=dict(radius=1, fill=True))
map.save(r'index.html')
