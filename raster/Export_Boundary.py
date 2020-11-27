%matplotlib inline
from osgeo import gdal,ogr
import pandas as pd
import geopandas
from shapely import wkt
import shutil


def ListofExtensionAndName(directory,extension):
     
        if len(directory) != None:
            import os
            FilesList = []
            FileName=[]
            for root, subdirectory, files in os.walk(directory):
                for file in files:
                    if file.endswith(extension):
                        FilesList.append(os.path.join(root,file))
                        base=os.path.basename(file)
                        FileName.append(os.path.splitext(base)[0])

            return FilesList,FileName
        else:
            print("no"+ extension +"file for this directory")

def ImageBoundry(FilePath):
        #for aspect data
        #imgname=FilePath

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
        return poly.ExportToJson() #,imgname


Polar_DEM=r"target images path"
Polar_List=ListofExtensionAndName(Polar_DEM,"tif")
shp_dst=r"export shape path"

#export images extend to .shp file
for index,img in enumerate(Polar_List[0],0):
    ImageBoundry_result=ImageBoundry(img)
    gdf_images = geopandas.read_file(ImageBoundry_result)
    geom_gdf_images=gdf_images.geometry
    geom_gdf_images.to_file(shp_dst+"/"+Polar_List[1][index]+".shp", driver='ESRI Shapefile', schema=None,)
    print(shp_dst+"/"+Polar_List[1][index]+".shp")





#code below, intersect the images according the target .shp and copy to intersect result to another folder.
ImageList=ListofExtensionAndName("path","extention")

gdf_eu = geopandas.read_file('''target shp file path''' )
#get the geometry of 
gdf_eu_geo=gdf_eu.geometry
#destination path for intersect images
dst=r"path"

for index,img in enumerate(ImageList[0],0):
    ImageBoundry_result=ImageBoundry(ImageList[0][index])
    gdf = geopandas.read_file(ImageBoundry_result)
    geom_gdf=gdf.geometry
    intersect4=geom_gdf.intersects(gdf_eu_geo)
    for i in intersect4:
        if i==True:
            print(img)
            shutil.copy(img,dst)

#export shp file of intersect images
shp_dst=r"path of shp file"

for index,img in enumerate(ImageList[0],0):
    ImageBoundry_result=ImageBoundry(ImageList[0][index])
    gdf = geopandas.read_file(ImageBoundry_result)
    geom_gdf=gdf.geometry
    intersect4=geom_gdf.intersects(gdf_eu_geo)
    for i in intersect4:
        if i==True:
            print(img)
            geom_gdf.to_file(shp_dst+"/"+ImageList[1][index]+".shp", driver='ESRI Shapefile', schema=None)

                
                


