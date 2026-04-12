# Proyecto 7: Tracker Promedio + Beca Tec
# BAIRON-DEV | RUTA USA 2030

print(">>> TRACKER PROMEDIO v1.0 <<<")
print("Calcula tu promedio y % beca Prepa Tec\n")

materias = {}
num_materias = int(input("Cuántas materias llevas?: "))

for i in range(num_materias):
    nombre = input(f"Nombre materia {i+1}: ")
    cali = float(input(f"Calificación de {nombre}: "))
    materias[nombre] = cali

promedio = sum(materias.values()) / len(materias)

# Lógica de beca STEAM 2027
beca = 0
if promedio >= 95: beca = 70
elif promedio >= 90: beca = 50
elif promedio >= 85: beca = 30
else: beca = 0

skills = int(input("\nCuántos skills extra tienes? Fútbol/Box/Música/Code: "))
beca += skills * 2
if beca > 90: beca = 90

print("\n" + "="*30)
print("REPORTE RUTA USA 2030")
print("="*30)
for mat, cal in materias.items():
    print(f"{mat}: {cal}")
print(f"\nPROMEDIO FINAL: {promedio:.2f}")
print(f"BECA ESTIMADA TEC: {beca}% 🏆")

if promedio == 100:
    print("STATUS: MODO DIOS ACTIVADO 💀")

# Guardamos como los robots
with open("reporte_beca.txt", "w") as f:
    f.write(f"PROMEDIO: {promedio:.2f}\nBECA: {beca}%\n")
    f.write("META: UT Austin 2030\n")
print("\nGuardado en reporte_beca.txt ✅")

