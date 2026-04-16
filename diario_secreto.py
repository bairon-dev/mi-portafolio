# Proyecto #12: Diario Secreto - 60%
# Autor: Bairon-Dev
# Fecha: 15 de abril 2026

def escribir_diario():
    print("=== DIARIO SECRETO BAIRON-DEV ===")
    entrada = input("¿Qué pasó hoy? Escribe tu secreto: ")
    
    # 'a' = append: agrega al final sin borrar lo anterior
    with open("mi_diario.txt", "a") as archivo:
        archivo.write(entrada + "\n")
    
    print("Guardado en mi_diario.txt. Nadie lo verá... o sí 😈")

def leer_diario():
    print("\n=== LEYENDO SECRETOS ===")
    try:
        # 'r' = read: solo leer
        with open("mi_diario.txt", "r") as archivo:
            contenido = archivo.read()
            if contenido == "":
                print("Tu diario está vacío. Escribe algo primero.")
            else:
                print(contenido)
    except FileNotFoundError:
        print("Aún no tienes diario. Escribe algo primero.")

# Menú principal
while True:
    print("\n1. Escribir secreto")
    print("2. Leer diario") 
    print("3. Salir")
    opcion = input("Elige 1, 2 o 3: ")
    
    if opcion == "1":
        escribir_diario()
    elif opcion == "2":
        leer_diario()
    elif opcion == "3":
        print("Cerrando diario... 🤐")
        break
    else:
        print("Opción inválida. Usa 1, 2 o 3.")

