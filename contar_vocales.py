# Proyecto #17: Contador de Vocales - 85%
# Autor: Bairon-Dev

def contar_vocales(texto):
    texto = texto.lower()
    a = texto.count('a')
    e = texto.count('e')
    i = texto.count('i')
    o = texto.count('o')
    u = texto.count('u')
    total = a + e + i + o + u
    return total, a, e, i, o, u

print("=== CONTADOR DE VOCALES BAIRON-DEV ===")
frase = input("Escribe una frase: ")
total, a, e, i, o, u = contar_vocales(frase)

print(f"\nTotal vocales: {total}")
print(f"a: {a} | e: {e} | i: {i} | o: {o} | u: {u}")

