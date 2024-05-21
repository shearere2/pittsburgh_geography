from osgeo import gdal
import numpy as np
from matplotlib import pyplot as plt
import rasterio as rio

# ds = gdal.Open('data/Allegheny_County_1m/PAMAP_DEM_mosaic_Allegheny_1m.tif')
# geotransform = ds.GetGeoTransform()
# proj = ds.GetProjection()

# band = ds.GetRasterBand(ds.RasterCount)
# array = band.ReadAsArray()

# plt.figure()
# plt.imshow(array)
# plt.savefig('data/pittsburgh')

dem = rio.open('data/Allegheny_County_1m/PAMAP_DEM_mosaic_Allegheny_1m.tif')
dem_array = dem.read(1).astype('float64')

fig, ax = plt.subplots(1, figsize=(12,12))
rio.plot.show(dem_array, cmap='Greys_r',ax=ax)
plt.axis('off')
plt.savefig('data/pittsburgh')