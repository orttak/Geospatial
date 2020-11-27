import fiona
import rasterio
import rasterio.mask

with fiona.open(r"C:\Users\akif.ortak\Desktop\World_Countries\north_extend\polar_world.shp") as shapefile:
    features = [feature["geometry"] for feature in shapefile]

with rasterio.open(r"C:\Users\akif.ortak\Desktop\deneme\EarthEnv-DEM90_N75E060.bil") as src:
    out_image, out_transform = rasterio.mask.mask(src, features,
                                                        crop=True)
out_meta = src.meta.copy()

out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform})
with rasterio.open("RGB.byte.masked.tif", "w", **out_meta) as dest:
    dest.write(out_image
