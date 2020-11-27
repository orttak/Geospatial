class GdalVectorProcess():

    def __init__(self,ULC=None, URC=None, LRC=None, LLC=None,SourceEPSG=4326,TargetEPSG=4326):
        self.ULC = ULC
        self.URC = URC
        self.LRC = LRC
        self.LLC = LLC
        self.SourceEPSG = SourceEPSG
        self.TargetEPSG = TargetEPSG

    def CreatePoligonBox(self):

        from osgeo import ogr
        ring = ogr.Geometry(ogr.wkbLinearRing)
        ring.AddPoint_2D(self.ULC[0], self.ULC[1])
        ring.AddPoint_2D(self.URC[0], self.URC[1])
        ring.AddPoint_2D(self.LRC[0], self.LRC[1])
        ring.AddPoint_2D(self.LLC[0], self.LLC[1])
        ring.AddPoint_2D(self.ULC[0], self.ULC[1]) 
        poly=ogr.Geometry(ogr.wkbPolygon)
        poly.AddGeometry(ring)
        return poly

    def CreateGeom2WKT(self,wkt):
     
        from osgeo import ogr
        poly = ogr.CreateGeometryFromWkt(wkt)
        return poly

    def ReferanceSystemChange(self):

        from osgeo import osr
        source = osr.SpatialReference()
        source.ImportFromEPSG(self.SourceEPSG)
        target = osr.SpatialReference()
        target.ImportFromEPSG(self.TargetEPSG)
        transform = osr.CoordinateTransformation(source, target)
        return transform


