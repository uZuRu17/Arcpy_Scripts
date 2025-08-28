# Functioneaza direct in ArcMap 10.x (Python 2.7)
import arcpy, random, math
from collections import Counter


#De modificat!
fc = r"C:\cale\catre\gdb.gdb"
nume_lista = ["Alex", "Bogdan", "Claudiu", "Darius"]
field_name = "Esantion"


#Nu modifica!
# 1) Asigură-te că există câmpul Esantion (TEXT)
if field_name not in [f.name for f in arcpy.ListFields(fc)]:
    arcpy.AddField_management(fc, field_name, "TEXT", field_length=30)

# 2) Calculează 10% aleatoriu
total_count = int(arcpy.GetCount_management(fc).getOutput(0))
if total_count == 0:
    raise ValueError("Layerul nu are înregistrări.")
sample_size = int(math.ceil(total_count * 0.10))

oid_field = arcpy.Describe(fc).OIDFieldName
all_oids = [r[0] for r in arcpy.da.SearchCursor(fc, [oid_field])]
sampled_oids = random.sample(all_oids, sample_size)

# 3) Distribuie numele cât mai egal
random.shuffle(sampled_oids)  # pentru a nu favoriza ordinea OID-urilor
base = sample_size // len(nume_lista)
remainder = sample_size % len(nume_lista)

assign_map = {}  # OID -> nume
start = 0
for i, name in enumerate(nume_lista):
    count = base + (1 if i < remainder else 0)
    for oid in sampled_oids[start:start+count]:
        assign_map[oid] = name
    start += count

# 4) Actualizează într-o singură trecere
updated = Counter()
with arcpy.da.UpdateCursor(fc, [oid_field, field_name]) as cursor:
    for row in cursor:
        oid = row[0]
        if oid in assign_map:
            row[1] = assign_map[oid]
            cursor.updateRow(row)
            updated[assign_map[oid]] += 1

print("Total obiecte: {}".format(total_count))
print("Esantion (10%): {}".format(sample_size))
for name in nume_lista:
    print("{}: {}".format(name, updated[name]))
