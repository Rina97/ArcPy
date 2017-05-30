import arcpy
from arcpy.sa import *
arcpy.env.workspace=r'C:\Users\User\Dropbox\Study\ProgPy\P1_3'
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
a=Idw(r'C:\Users\User\Dropbox\Study\ProgPy\Lesson1\Precip2008Readings.shp','RASTERVALU')
b=Reclassify(a,'Value',RemapRange([[27715,55521,1],[55521,83326,2],[83326,111133,3]]))
arcpy.RasterToPolygon_conversion(b,r'C:\Users\User\Dropbox\Study\ProgPy\P1_3\P1\poly.shp',"NO_SIMPLIFY",'VALUE')
arcpy.Clip_analysis(r'C:\Users\User\Dropbox\Study\ProgPy\P1_3\poly.shp',
                    r'C:\Users\User\Dropbox\Study\ProgPy\Lesson1\Nebraska.shp',
                    r'C:\Users\User\Dropbox\Study\ProgPy\P1_3\polyclip.shp')
