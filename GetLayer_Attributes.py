sum = 0.0
for row in arcpy.SearchCursor("Sector_Cadastral"):
     sup = sup+row.Shape_Area
     
print sum
