import arcpy
import os
arcpy.env.workspace = arcpy.GetParameterAsText(0)
target=arcpy.GetParameterAsText(1)
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    desc = arcpy.Describe(fc)
    if desc.spatialReference.name!=arcpy.Describe(target).spatialReference.name:
        outfc=desc.name[:-4]+'_projected.shp'
        arcpy.Project_management(fc,os.path.join(arcpy.env.workspace,outfc),arcpy.Describe(target).spatialReference)
    #arcpy.AddMessage(desc.spatialReference.name)

print "Script completed"
