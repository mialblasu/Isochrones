#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      omar
#
# Created:     06-04-2013
# Copyright:   (c) omar 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy

from math import radians, sin, cos

origin_x, origin_y = (400460.99, 135836.7)
distance = 800
angle = 15 # in degrees

# calculate offsets with light trig
(disp_x, disp_y) = (distance * sin(radians(angle)),\
                    distance * cos(radians(angle)))
(end_x, end_y) = (origin_x + disp_x, origin_y + disp_y)

output = "offset-line.shp"
arcpy.CreateFeatureClass_management("c:\workspace", output, "Polyline")
cur = arcpy.InsertCursor(output)
lineArray = arcpy.Array()

# start point
start = arcpy.Point()
(start.ID, start.X, start.Y) = (1, origin_x, origin_y)
lineArray.add(start)

# end point
end = arcpy.Point()
(end.ID, end.X, end.Y) = (2, end_x, end_y)
lineArray.add(end)

# write our fancy feature to the shapefile
feat = cur.newRow()
feat.shape = lineArray
cur.insertRow(feat)

# yes, this shouldn't really be necessary...
lineArray.removeAll()
del cur