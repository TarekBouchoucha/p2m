import geopandas as gpd
from shapely.geometry import Polygon, MultiPolygon

# Read the shapefile into a GeoDataFrame
gdf = gpd.read_file('data/raw_data/wildfires-ground-truth/portugal/ardida_2016.shp')

# Initialize counters for polygons and multipolygons
polygon_count = 0
multipolygon_count = 0

# Iterate over the geometries and count polygons and multipolygons
for geometry in gdf['geometry']:
    if isinstance(geometry, Polygon):
        polygon_count += 1
    elif isinstance(geometry, MultiPolygon):
        multipolygon_count += 1

# Print the counts of polygons and multipolygons
print("Number of polygons:", polygon_count)
print("Number of multipolygons:", multipolygon_count)