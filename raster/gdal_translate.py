from osgeo import gdal
import os
import geopandas

def ListofExtention(directory,extension):
     
        if len(directory) != None:
            import os
            FilesList = []
            for root, subdirectory, files in os.walk(directory):
                for file in files:
                    if file.endswith(extension):
                        FilesList.append(os.path.join(root,file))

            return FilesList
        else:
            print("no"+ extension +"file for this directory")

        
def ListofExtensionAndName(directory,extension):
     
    if len(directory) != None:
                
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


#in below, you can convert rater file according your working area. 

#import shapefile and get geometry
countries=geopandas.read_file(r"C:\Users\akif.ortak\Desktop\World_Countries\gdam_world_borders_grid\gdam_world_borders_grid.shp")
geom_country=countries.geometry
#get list of image file path and their name
ImageList=ListofExtensionAndName(r"D:\elevation_N60ton80",".bil")

for index,img in enumerate(ImageList[0],0):
    #get image and calculate geometry
    ImageBoundry_result=ImageBoundry(ImageList[0][index])
    gdf = geopandas.read_file(ImageBoundry_result)
    geom_gdf=gdf.geometry
    for i in range(len(geom_country)):
        intersect4=geom_gdf.intersects(geom_country[i])
        for i in intersect4:
            if i==True:
                targetimg = gdal.Open(img)
                #define your output path and extension
                outputname=r"D:\elevation_N60ton80_intersectResult\\"+ImageList[1][index] +".tif"
                outputimg = gdal.Translate( outputname,targetimg)



#gdal translate using in python code or jupyter.
gdalinput = tile+'.tif'
gdaloutput = oFolder+'\\'+Path(tile).name+'.tif'    
translateoptions = gdal.TranslateOptions(gdal.ParseCommandLine("-ot Int16 -of Gtiff "))
gdal.Translate(gdaloutput, gdalinput, options=translateoptions)






