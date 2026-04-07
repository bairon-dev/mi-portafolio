# Calculadora Simple - Proyecto 2 de Bairon Daniel
# Portafolio para PrepaTec

print("=== MI CALCULADORA ===")
print("Bairon Daniel - Futuro Ingeniero de Software")
print("")

# Pedimos los números
num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))

print("")
print("=== RESULTADOS ===")
print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)

# Cuidado con división entre cero
if num2 != 0:
    print("División:", num1 / num2)
else:
    print("División: No se puede dividir entre cero")

print("")
print("¡Gracias por u
