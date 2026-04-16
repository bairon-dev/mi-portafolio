# Proyecto #20: Clase Persona - 100% GRADUADO
# Autor: Bairon-Dev

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")
    
    def es_mayor(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad ✅")
        else:
            print(f"{self.nombre} es menor de edad 🔒")

print("=== POO BAIRON-DEV ===")
dev1 = Persona("Bairon", 21)
dev1.saludar()
dev1.es_mayor()

dev2 = Persona("Meta AI", 1)
dev2.saludar()
dev2.es_mayor()

