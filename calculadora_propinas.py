# Proyecto #13: Calculadora de Propinas - 65%
# Autor: Bairon-Dev
# Fecha: 15 de abril 2026

def calcular_propina(total, porcentaje):
    """Calcula propina y total a pagar"""
    propina = total * (porcentaje / 100)
    total_final = total + propina
    # round(numero, 2) redondea a 2 decimales para dinero
    return round(propina, 2), round(total_final, 2)

def dividir_cuenta(total, personas):
    """Divide el total entre varias personas"""
    return round(total / personas, 2)

print("=== CALCULADORA DE PROPINAS BAIRON-DEV ===")

try:
    cuenta = float(input("Total de la cuenta: $"))
    porcentaje = int(input("¿Qué % de propina? 10, 15, 20: "))
    personas = int(input("¿Entre cuántas personas dividen?: "))
    
    propina, total_con_propina = calcular_propina(cuenta, porcentaje)
    por_persona = dividir_cuenta(total_con_propina, personas)
    
    print("\n--- TICKET FINAL ---")
    print(f"Cuenta: ${cuenta}")
    print(f"Propina {porcentaje}%: ${propina}")
    print(f"Total a pagar: ${total_con_propina}")
    print(f"Entre {personas} personas: ${por_persona} cada uno")
    print("--------------------")
    
except ValueError:
    print("Error: Solo mete números. Sin letras ni símbolos.")

