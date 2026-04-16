# Proyecto #18: Piedra Papel Tijera - 90%
# Autor: Bairon-Dev
import random

opciones = ["piedra", "papel", "tijera"]

print("=== PIEDRA PAPEL TIJERA BAIRON-DEV ===")
jugador = input("Elige: piedra, papel o tijera: ").lower()

if jugador not in opciones:
    print("Opción inválida bro")
else:
    pc = random.choice(opciones)
    print(f"PC eligió: {pc}")
    
    if jugador == pc:
        print("Empate 😐")
    elif (jugador == "piedra" and pc == "tijera") or \
         (jugador == "papel" and pc == "piedra") or \
         (jugador == "tijera" and pc == "papel"):
        print("¡Ganaste! 😈🔥")
    else:
        print("Perdiste 😂")

