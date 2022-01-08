import json
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import folium as f

with open(r".\data\result.json") as file:
    data = json.load(file)

df = pd.DataFrame({
    "Name": [city["city_ascii"] for city in data],
    "Country": [city["country"] for city in data],
    "Population": [city["population"] for city in data],
    "Latitude": [city["lat"] for city in data],
    "Longitude": [city["lng"] for city in data]
})

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))

bg = f.Map()
map = gdf.explore(m=bg, marker_kwds=dict(radius=2, fill=True))
map.save(r'.\data\map.html')