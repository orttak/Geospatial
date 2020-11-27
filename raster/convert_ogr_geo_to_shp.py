def write_geometry(geometry, out_path, srs_id=4326):
    """
    Saves the geometry in an ogr.Geometry object to a shapefile.

    Parameters
    ----------
    geometry
        An ogr.Geometry object
    out_path
        The location to save the output shapefile
    srs_id
        The projection of the output shapefile. Can be an EPSG number or a WKT string.

    Notes
    -----
    The shapefile consists of one layer named 'geometry'.


    """
    # TODO: Fix this needing an extra filepath on the end
    driver = ogr.GetDriverByName("ESRI Shapefile")
    data_source = driver.CreateDataSource(out_path)
    srs = osr.SpatialReference()
    if type(srs_id) is int:
        srs.ImportFromEPSG(srs_id)
    if type(srs_id) is str:
        srs.ImportFromWkt(srs_id)
    layer = data_source.CreateLayer(
        "geometry",
        srs,
        geom_type=geometry.GetGeometryType())
    feature_def = layer.GetLayerDefn()
    feature = ogr.Feature(feature_def)
    feature.SetGeometry(geometry)
    layer.CreateFeature(feature)
    data_source.FlushCache()
    data_source = None 