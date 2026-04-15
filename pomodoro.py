import time

def pomodoro():
    print("🍅 POMODORO BAIRON-DEV - MODO PREPATEC ON")
    
    ciclos = int(input("¿Cuántos ciclos de 25min quieres? "))
    
    for i in range(ciclos):
        print(f"\n📚 CICLO {i+1}/{ciclos}: 25 MIN DE ESTUDIO - FOCUS")
        for min_restante in range(25, 0, -1):
            print(f"Tiempo: {min_restante} min", end="\r")
            time.sleep(60)  # 60 seg = 1 min real
        
        print("\n✅ CICLO TERMINADO")
        
        if i < ciclos - 1:  # Si no es el último
            print("☕ DESCANSO 5 MIN - RESPIRA")
            for min_descanso in range(5, 0, -1):
                print(f"Descanso: {min_descanso} min", end="\r")
                time.sleep(60)
    
    print("\n🏆 META CUMPLIDA, BAIRON-DEV. A descansar como campeón")

if __name__ == "__main__":
    pomodoro()

