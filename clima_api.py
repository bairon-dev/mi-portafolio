# Proyecto #19: API del Clima - 95%
# Autor: Bairon-Dev
import requests

print("=== CLIMA BAIRON-DEV ===")
ciudad = input("Escribe tu ciudad: ")

try:
    url = f"https://wttr.in/{ciudad}?format=3"
    respuesta = requests.get(url)
    print(f"\nClima: {respuesta.text}")
except:
    print("Error: Instala requests con 'pip install requests'")

