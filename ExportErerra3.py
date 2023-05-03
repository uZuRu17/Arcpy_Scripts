import time
import os
import ftplib
import shutil
import arcpy
from datetime import datetime


print("se descarca:")
filename = 'ImobileE3.zip'
filename1 = 'ConstructiiE3.zip'
if os.path.isfile(filename):
    os.remove(filename)
if os.path.isfile(filename1):
    os.remove(filename1)

print("ImobileE3")
ftp = ftplib.FTP("10.0.1.69")
ftp.login("utilizator", "parola")
ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
size = ftp.size(filename)
if (os.path.getsize(filename)!=size):
    time.sleep(1)
else:
    print("ConstructiiE3")
    ftp.retrbinary("RETR " + filename1, open(filename1, 'wb').write)
ftp.quit()

today = 'Eterra_'+datetime.now().strftime('%Y_%m_%d')
root = r"\\Mh0sv08\d\Cadastru\Diverse date\Export_Eterra"
my_folder = root + '/' + today
filepath = my_folder + '/' + filename
filepath1 = my_folder + '/' + filename1
if not os.path.exists(my_folder):
    os.makedirs(my_folder)

#dezarhiveaza
print("Se dezarhiveaza:")
print("ImobileE3")
shutil.unpack_archive(filename,my_folder)
print("ConstructiiE3")
shutil.unpack_archive(filename1,my_folder)


#Sterge geometriile inactive
print("Se seteaza spatiu de lucru pentru ImobileE3")
arcpy.env.workspace = my_folder + '/' + 'ImobileE3.gdb'

print("Se selecteaza imobile active")
arcpy.SelectLayerByAttribute_management('ImobileE3', 'NEW_SELECTION','"IS_ACTIVE" = 1 AND "STATUS" = 1')
print("Se inverseaza selectia")
arcpy.SelectLayerByAttribute_management('ImobileE3', 'SWITCH_SELECTION')

print("Se creaza feature class nou")
# Write the selected features to a new featureclass
arcpy.CopyFeatures_management('ImobileE3_Layer2', 'ImobileE3Active')

#Sterge geometriile inactive
print("Se seteaza spatiu de lucru pentru ConstructiiE3")
arcpy.env.workspace = my_folder + '/' + 'ConstructiiE3.gdb'

print("Se selecteaza imobile active")
arcpy.SelectLayerByAttribute_management('ConstructiiE3', 'NEW_SELECTION','"IS_ACTIVE" = 1 AND "STATUS" = 1')
arcpy.SelectLayerByAttribute_management('ConstructiiE3', 'SWITCH_SELECTION')

print("Se creaza feature class nou")
# Write the selected features to a new featureclass
arcpy.CopyFeatures_management('ConstructiiE3_Layer2', 'ConstructiiE3Active')
