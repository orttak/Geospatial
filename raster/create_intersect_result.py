from osgeo import gdal
import os
import geopandas


def ImageBoundry(FilePath):

        from osgeo import gdal,ogr
        ds = gdal.Open(FilePath)
        gt = ds.GetGeoTransform()  # captures origin and pixel size

        ULC = gdal.ApplyGeoTransform(gt, 0, 0) #Upper Left Corner
        URC = gdal.ApplyGeoTransform(gt, ds.RasterXSize, 0) #Upper Right Corner
        LLC = gdal.ApplyGeoTransform(gt, 0, ds.RasterYSize) #Lower Left Corner
        LRC = gdal.ApplyGeoTransform(gt, ds.RasterXSize, ds.RasterYSize) #Lower Right Corner
                   
        ring = ogr.Geometry(ogr.wkbLinearRing)
        ring.AddPoint_2D(ULC[0], ULC[1])
        ring.AddPoint_2D(URC[0], URC[1])
        ring.AddPoint_2D(LRC[0], LRC[1])
        ring.AddPoint_2D(LLC[0], LLC[1])
        ring.AddPoint_2D(ULC[0], ULC[1]) 
        poly=ogr.Geometry(ogr.wkbPolygon)
        poly.AddGeometry(ring)
        poly.ExportToJson
        return poly.ExportToJson()

countries=geopandas.read_file(r"gdam_world_borders_grid.shp")
imageboundry_subset=ImageBoundry(r"EarthEnv-DEM90_N60E020.bil")
gdf = geopandas.read_file(imageboundry_subset)
geom_gdf=gdf.geometry
geom_country=countries.geometry
res_intersection = geopandas.overlay(countries,gdf, how='intersection')
res_intersection.to_file("intersect", driver='ESRI Shapefile', schema=None,)

