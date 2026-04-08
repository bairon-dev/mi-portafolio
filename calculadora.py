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

