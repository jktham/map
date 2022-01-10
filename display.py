import json

import folium
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry.linestring import LineString

with open(r".\data\sorted.json") as file:
    data = json.load(file)

df_points = pd.DataFrame({
    "Name": [city["city_ascii"] for city in data],
    "Country": [city["country"] for city in data],
    "Population": [city["population"] for city in data],
    "Latitude": [city["lat"] for city in data],
    "Longitude": [city["lng"] for city in data]
})

start = []
end = []
geom_lines = []

for i in range(len(data)):
    j = 1
    if data[i]["city_ascii"] != data[i-1]["city_ascii"]:
        while data[i+j]["city_ascii"] == data[i]["city_ascii"]:
            start.append(f"{data[i]['city_ascii']}, {data[i]['admin_name']}, {data[i]['country']} ({data[i]['population']}) [{1}/{[city['city_ascii'] for city in data].count(data[i]['city_ascii'])}]")
            end.append(f"{data[i+j]['city_ascii']}, {data[i+j]['admin_name']}, {data[i+j]['country']} ({data[i+j]['population']}) [{j+1}/{[city['city_ascii'] for city in data].count(data[i]['city_ascii'])}]")
            geom_lines.append(LineString(coordinates=((float(data[i]["lng"]), float(data[i]["lat"])), (float(data[i+j]["lng"]), float(data[i+j]["lat"])))))
            j += 1
            if i+j == len(data):
                break

df_lines = pd.DataFrame({
    "From": start,
    "To": end,
})

gdf_points = gpd.GeoDataFrame(df_points, geometry=gpd.points_from_xy(df_points.Longitude, df_points.Latitude))
gdf_lines = gpd.GeoDataFrame(df_lines, geometry=geom_lines)

map = folium.Map()
map = gdf_points.explore(m=map, marker_kwds=dict(radius=0.5, fill=True, opacity=0.2))
map = gdf_lines.explore(m=map, style_kwds=dict(weight=0.5, color="red", opacity=0.1), highlight_kwds=dict(weight=1, color="yellow", opacity=1.0))
map.save(r'index.html')
