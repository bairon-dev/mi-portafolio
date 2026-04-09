def ver_tareas():
    try:
        with open("tareas.txt", "r") as archivo:
            tareas = archivo.readlines()
            if not tareas:
                print("No tienes tareas pendientes 💀")
            else:
                print("\n--- TUS TAREAS ---")
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea.strip()}")
    except FileNotFoundError:
        print("No tienes tareas pendientes 💀")

def agregar_tarea():
    tarea = input("Escribe la nueva tarea: ")
    with open("tareas.txt", "a") as archivo:
        archivo.write(tarea + "\n")
    print("Tarea agregada ✅")

def borrar_tareas():
    with open("tareas.txt", "w") as archivo:
        pass
    print("Todas las tareas borradas 💀")

while True:
    print("\n=== LISTA DE TAREAS BAIRON-DEV ===")
    print("1. Ver tareas")
    print("2. Agregar tarea") 
    print("3. Borrar todas las tareas")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        ver_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        borrar_tareas()
    elif opcion == "4":
        print("¡Nos vemos! Sigue codeando para la Beca STEAM 🚀")
        break
