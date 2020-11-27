#below code lines are last code of subset the aspect mosaic. 
#We can define two different height and weight for the image because different size of images
#north 60 to 80 data have 6000*6000 but others have 6001*6001.

Targetimage3=  #mosaic aspect
SlopeSubset3= #subset image path
RawImagePath3= #raw dem data for getting extention
RawImagePath4= #raw dem data for getting extention

SubsetListName3=ListofExtensionAndName(Targetimage3,"tif")

SubsetListName3[1][0:10][0][0] #name of the rawimage

for index,i in enumerate(SubsetListName3[0],0):
    targetimagepath=i
    if SubsetListName3[1][index][0][0]=='E':
        rawimagepath=RawImagePath4+"/"+SubsetListName3[1][index]+".tif"
        subsetimagepath=SlopeSubset3+"/"+SubsetListName3[1][index]+".tif"
        print("------- raw image -----------------")
        print(rawimagepath)
        print("------- new image -----------------")
        print(subsetimagepath)
        
        
        imageboundry_subset=ImageBoundry(rawimagepath) #get the boudry
        gdf = geopandas.read_file(imageboundry_subset)
        geom_gdf=gdf.geometry
        
        print(geom_gdf)
        #geom_gdf.to_file(r"C:/Users/akif.ortak/Desktop/deneme/extendwholeimages"+"/"+SubsetListName2[1][index]+".shp", driver='ESRI Shapefile', schema=None,)
    
        #print(r"C:/Users/akif.ortak/Desktop/deneme/extendwholeimages"+"/"+SubsetListName2[1][index]+".shp")
        print("---------------------------------")
        
        with rasterio.open(targetimagepath) as src:
            #open target image
            out_image, out_transform = rasterio.mask.mask(src, geom_gdf,
                                                          crop=True) #subset the image according to new extend
        out_meta = src.meta.copy()
        height=6000
        width=6000
        
        if out_image.shape[1] != height or out_image.shape[2]!=width:
            out_meta.update({"driver": "GTiff",
                             "height": height,
                             "width": width,
                             "transform": out_transform})
        
            with rasterio.open(subsetimagepath, "w", **out_meta) as dest:
                dest.write(out_image) #save the new subset image 
    
    
    
    else :
        rawimagepath=RawImagePath3+"/"+SubsetListName3[1][index]+".tif"
        subsetimagepath=SlopeSubset3+"/"+SubsetListName3[1][index]+".tif"
        print("------- raw image -----------------")
        print(rawimagepath)
        print("------- new image -----------------")
        print(subsetimagepath)
        
        
        imageboundry_subset=ImageBoundry(rawimagepath) #get the boudry
        gdf = geopandas.read_file(imageboundry_subset)
        geom_gdf=gdf.geometry
        
        #print(geom_gdf)
        #geom_gdf.to_file(r"C:/Users/akif.ortak/Desktop/deneme/extendwholeimages"+"/"+SubsetListName2[1][index]+".shp", driver='ESRI Shapefile', schema=None,)
    
        #print(r"C:/Users/akif.ortak/Desktop/deneme/extendwholeimages"+"/"+SubsetListName2[1][index]+".shp")
        print("---------------------------------")
        
        with rasterio.open(targetimagepath) as src:
            #open target image
            out_image, out_transform = rasterio.mask.mask(src, geom_gdf,
                                                          crop=True) #subset the image according to new extend
        out_meta = src.meta.copy()
        height=6001
        width=6001

        ''' we can define output raster's extend with below codes. If we know the extend of the raw images, it is better option.
        "height": out_image.shape[1],
        "width": out_image.shape[2],
        '''
        
        if out_image.shape[1] != height or out_image.shape[2]!=width:
            out_meta.update({"driver": "GTiff",
                             "height": height,
                             "width": width,
                             "transform": out_transform})
        
            with rasterio.open(subsetimagepath, "w", **out_meta) as dest:
                dest.write(out_image) #save the new subset image 
        
        
    