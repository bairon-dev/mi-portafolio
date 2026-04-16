# Proyecto #15: Lista de Compras - 75%
# Autor: Bairon-Dev

compras = []

print("=== LISTA DE COMPRAS BAIRON-DEV ===")
print("Escribe 'salir' para terminar")

while True:
    item = input("Agrega un artículo: ")
    if item.lower() == "salir":
        break
    compras.append(item)
    print(f"Agregado: {item}")

print("\n--- TU LISTA FINAL ---")
if len(compras) == 0:
    print("Lista vacía. ¿Dieta o qué? 😂")
else:
    for i, producto in enumerate(compras, 1):
        print(f"{i}. {producto}")
    print(f"Total: {len(compras)} artículos")

