import json
import matplotlib.pyplot as plt
import geopandas as gpd
import folium as f

with open(r".\data\result.json") as file:
    data = json.load(file)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
m = world.explore()
m.save('map.html')