import random
print("🎲 Simulador de Dados - By BaironDev")
input("Presiona Enter para lanzar...")
dado = random.randint(1, 6)
print(f"Salió: {dado}")
if dado == 6:
    print("¡Crítico! Sacaste 6 🚀")
elif dado == 1:
    print("Mala suerte... sacaste 1 😅")
else:
    print("Nada mal 👍")
