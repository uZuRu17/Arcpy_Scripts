#Selecteaza Sectoarele
arcpy.SelectLayerByAttribute_management("Sector_Cadastral","NEW_SELECTION",""" "Nr_SC" In (13,17,2,9) """)
#reseteaza suma suprafetelor
sum = 0.0
for row in arcpy.SearchCursor("Sector_Cadastral"):
    sum = sum+row.Shape_Area
      
#arata rezultat
print sum
#nu uita sa deselectezi daca mai lucrezi cu layerul asta
