sum = 0.0
for row in arcpy.SearchCursor("Sector_Cadastral"):
     sup = sum+row.Shape_Area
     
print sum
