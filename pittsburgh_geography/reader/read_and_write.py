from osgeo import gdal
import numpy as np
from matplotlib import pyplot as plt

ds = gdal.Open('data/Allegheny_County_1m/PAMAP_DEM_mosaic_Allegheny_1m.tif')
geotransform = ds.GetGeoTransform()
proj = ds.GetProjection()

band = ds.GetRasterBand(ds.RasterCount)
array = band.ReadAsArray()

plt.figure()
plt.imshow(array)