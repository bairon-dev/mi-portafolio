import random

print("=== GENERADOR DE MEMES TEXTO - BAIRON-DEV ===")

def generar_meme():
    frase = input("Escribe tu frase mamalona: ").upper()
    
    estilos = {
        "grito": f"¡¡{frase}!!!",
        "dramatico": f"{frase}...\n{frase}...\n¡¡{frase}!!!",
        "ascii": f"+{'-' * (len(frase)+2)}+\n| {frase} |\n+{'-' * (len(frase)+2)}+",
        "espaciado": " ".join(frase),
        "temblor": f"~{frase}~ ¿o KÉ?"
    }
    
    print("\n=== TU MEME LISTO ===")
    estilo_random = random.choice(list(estilos.keys()))
    print(f"Estilo: {estilo_random}")
    print(estilos[estilo_random])
    
    print("\n=== TODOS LOS ESTILOS ===")
    for nombre, texto in estilos.items():
        print(f"\n{nombre}:")
        print(texto)

generar_meme()
print("\nProyecto #11/20 - 55% completado 💀🚀")

