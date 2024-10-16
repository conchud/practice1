import os
import geopandas as gpd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

class CensusTract:
    def __init__(self, geoid, population, geometry):
        self.geoid = geoid
        self.population = population
        self.geometry = geometry
    
    def calculate_population_density(self):
        # Calculate the population density 
        area = self.geometry.area  # use area of geometry
        if area > 0:
            population_density = self.population / area
        else:
            population_density = 0
        return population_density

if __name__ == "__main__":
    file_path = os.path.join(DATA_DIR, 'data.geojson')
    gdf = gpd.read_file("C:/Users/Mango/OneDrive/Desktop/python Geog392/data.geojson")
    print(gdf.head())
    print(gdf.columns)
    print(gdf.shape)
    print(gdf.dtypes)


    def calculate_density(row):
        census_tract = CensusTract(row['GeoId'], row['Pop'], row['geometry'])
        return census_tract.calculate_population_density()

   
    gdf['Pop_Den_new'] = gdf.apply(calculate_density, axis=1)

   
    print(gdf.head())