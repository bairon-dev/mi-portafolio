<<<<<<< HEAD
print("=== CALCULADORA CERBERO V1 ===")
print("Operaciones: +  -  *  /")

num1 = float(input("Primer número: "))
operacion = input("Operación: ")
num2 = float(input("Segundo número: "))

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: No se divide entre 0"
else:
    resultado = "Operación no válida cerbero"

print(f"Resultado: {resultado}")
print("Gracias por usar Calculadora Cerbero 🚀")

=======
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
>>>>>>> d0000a260f4640b2fb3565341cbfde9c62f297f7
