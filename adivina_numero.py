import random

numero_secreto = random.randint(1, 10)
intentos = 0
adivinado = False

print("=== ADIVINA EL NÚMERO ===")
print("Estoy pensando un número del 1 al 10")

while adivinado == False:
    mi_numero = int(input("¿Cuál crees que es?: "))
    intentos = intentos + 1
    
    if mi_numero == numero_secreto:
        print(f"¡CORRECTO! Era {numero_secreto}")
        print(f"Lo lograste en {intentos} intentos")
        adivinado = True
    elif mi_numero < numero_secreto:
        print("Muy bajo. Intenta más alto ⬆️")
    else:
        print("Muy alto. Intenta más bajo ⬇️")

print("Gracias por jugar, cerbero 🚀")

