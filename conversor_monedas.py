# Proyecto #16: Conversor de Monedas - 80%
# Autor: Bairon-Dev

tasas = {
    "USD": 1.0,
    "MXN": 17.5,
    "EUR": 0.92,
    "JPY": 149.5
}

print("=== CONVERSOR BAIRON-DEV ===")
print("Monedas: USD, MXN, EUR, JPY")

try:
    cantidad = float(input("Cantidad a convertir: $"))
    origen = input("De qué moneda?: ").upper()
    destino = input("A qué moneda?: ").upper()
    
    if origen in tasas and destino in tasas:
        en_usd = cantidad / tasas[origen]
        resultado = en_usd * tasas[destino]
        print(f"\n${cantidad} {origen} = ${round(resultado, 2)} {destino}")
    else:
        print("Moneda no válida. Usa USD, MXN, EUR, JPY")
except ValueError:
    print("Solo números en la cantidad.")

