# Proyecto #14: Adivinador de Edad - 70%
# Autor: Bairon-Dev
from datetime import datetime

def calcular_edad(año_nacimiento):
    año_actual = datetime.now().year
    edad = año_actual - año_nacimiento
    return edad

print("=== ADIVINADOR DE EDAD BAIRON-DEV ===")
try:
    año = int(input("¿En qué año naciste?: "))
    edad = calcular_edad(año)
    
    if edad < 0:
        print("Bro... ¿vienes del futuro? 🤖")
    elif edad > 120:
        print("¿Eres vampiro? Respeta 👴")
    else:
        print(f"Tienes {edad} años aproximadamente")
        if edad >= 18:
            print("Eres mayor de edad ✅")
        else:
            print("Menor de edad 🔒")
except ValueError:
    print("Mete un año válido. Solo números.")

