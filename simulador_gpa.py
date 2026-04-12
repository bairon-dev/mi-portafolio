# Proyecto 8/20: Simulador GPA USA - Ruta USA 2030
# Autor: Bairon-dev

print("=== SIMULADOR GPA ESTILO USA - UT AUSTIN MODE ===")

def letra_a_puntos(letra):
    escala = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    return escala.get(letra.upper(), 0.0)

total_puntos = 0
total_creditos = 0

num_materias = int(input("¿Cuántas materias llevas este semestre?: "))

for i in range(num_materias):
    print(f"\n--- Materia {i+1} ---")
    creditos = int(input("Créditos de la materia: "))
    calif = input("Calificación final A/B/C/D/F: ")
    
    puntos = letra_a_puntos(calif)
    total_puntos += puntos * creditos
    total_creditos += creditos

if total_creditos == 0:
    print("Error: Créditos no pueden ser 0")
else:
    gpa = total_puntos / total_creditos
    print(f"\n=== RESULTADO ===")
    print(f"Créditos totales: {total_creditos}")
    print(f"GPA del semestre: {gpa:.2f}")
    
    if gpa >= 3.5:
        print("Status: Dean's List. Eres crack, modo honors.")
    elif gpa >= 3.0:
        print("Status: On Track. Buen camino para beca.")
    elif gpa >= 2.0:
        print("Status: A salvo. Pero métele más gas.")
    else:
        print("Status: Academic Probation. Aguas con la beca.")

print("\nRuta USA 2030: Entiendes el sistema antes de llegar.")

