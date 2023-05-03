#Clear Selection
#arcpy.SelectLayerByAttribute_management("Layer","CLEAR_SELECTION")
arcpy.SelectLayerByAttribute_management("Sector_Cadastral","CLEAR_SELECTION")

#Selection
arcpy.SelectLayerByAttribute_management("Layer","NEW_SELECTION",""" "Attribute" %works like fild calculator% """)
arcpy.SelectLayerByAttribute_management("Sector_Cadastral","NEW_SELECTION",""" "Nr_SC" In (13,17,2,9) """)
