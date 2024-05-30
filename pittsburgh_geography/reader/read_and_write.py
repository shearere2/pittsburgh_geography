from osgeo import gdal
import numpy as np
from matplotlib import pyplot as plt
from osgeo import ogr
from osgeo.gdal import OpenEx
driver = ogr.GetDriverByName("OpenFileGDB")
ds = driver.Open(r"data/PAAlleghenyCo_Terrain_DEM2017.gdb", 0)

# Need to be able to understand how to use "ds"