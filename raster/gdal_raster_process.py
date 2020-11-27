class GdalRasterProcess():

    def __init__(self,FilePath):
        self.FilePath = FilePath   #raster data full path>>>> home/raster/image.tif


    def GdalOpen(self):
        from osgeo import gdal
        ds = gdal.Open(self.FilePath)   #open image file
        return ds

    def ImageBoundry(self):

        from osgeo import gdal
        ds = gdal.Open(self.FilePath)
        gt = ds.GetGeoTransform()  # captures origin and pixel size

        ULC = gdal.ApplyGeoTransform(gt, 0, 0) #Upper Left Corner
        URC = gdal.ApplyGeoTransform(gt, ds.RasterXSize, 0) #Upper Right Corner
        LLC = gdal.ApplyGeoTransform(gt, 0, ds.RasterYSize) #Lower Left Corner
        LRC = gdal.ApplyGeoTransform(gt, ds.RasterXSize, ds.RasterYSize) #Lower Right Corner
        return ULC, URC, LRC, LLC

    def PixelSize(self):

        from osgeo import gdal
        ds = gdal.Open(self.FilePath)
        gt = ds.GetGeoTransform()  # captures origin and pixel size
        print("Image name " + self.FilePath)
        print('Pixel size:', (gt[1], gt[5]))
        PixelSize = gt[1], gt[5]
        return PixelSize






