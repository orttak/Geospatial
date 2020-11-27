from osgeo import gdal
input_raster = r"C:\Users\akif.ortak\Desktop\Slope\slope_earthenv\EarthEnv-DEM90_N60E000.tif" 
# or as an alternative if the input is already a gdal raster object you can use that gdal object
input_raster=gdal.Open(r"C:\Users\akif.ortak\Desktop\Slope\slope_earthenv\EarthEnv-DEM90_N60E000.tif")
input_shape = r"C:\Users\akif.ortak\Desktop\World_Countries\countries_border.shp" # or any other format
output_raster=r"C:\Users\akif.ortak\Desktop\outputDEM.tif" #your output raster file

ds = gdal.Warp(output_raster,
              input_raster,
              format = 'GTiff',
              cutlineDSName = input_shape, # or any other file format
              cutlineWhere="FIELD = 'whatever'" # optionally you can filter your cutline (shapefile) based on attribute values
              ) # select the no data value you like
ds=None #do other stuff with ds object, it is your cropped dataset. in this case we only close the dataset