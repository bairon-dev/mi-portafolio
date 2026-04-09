import random
import string

print("🔐 GENERADOR DE CONTRASEÑAS BAIRON-DEV v1.0")
print("=" * 45)

try:
    longitud = int(input("¿De cuántos caracteres? (8-20 recomendado): "))
    
    if longitud < 4:
        print("❌ Mínimo 4 caracteres por seguridad")
        exit()
    elif longitud > 50:
        print("❌ Máximo 50, no exageres 😂")
        exit()
except ValueError:
    print("❌ Usa solo números")
    exit()

print("\n¿Qué debe incluir tu contraseña?")
mayus = input("¿Mayúsculas? (s/n): ").lower() == 's'
minus = input("¿Minúsculas? (s/n): ").lower() == 's'
numeros = input("¿Números? (s/n): ").lower() == 's'
simbolos = input("¿Símbolos? !@#$% (s/n): ").lower() == 's'

caracteres = ""
if mayus: caracteres += string.ascii_uppercase
if minus: caracteres += string.ascii_lowercase  
if numeros: caracteres += string.digits
if simbolos: caracteres += "!@#$%^&*()_+-=[]{}|;:,.<>?"

if caracteres == "":
    print("\n❌ Elige al menos una opción")
    exit()

contraseña = ""
for i in range(longitud):
    contraseña += random.choice(caracteres)

print("\n" + "=" * 45)
print("✅ CONTRASEÑA GENERADA:")
print(f"🔑 {contraseña}")
print("=" * 45)
print("⚠️  Guárdala en un lugar seguro")
print("🚀 BaironDev Security Systems")
