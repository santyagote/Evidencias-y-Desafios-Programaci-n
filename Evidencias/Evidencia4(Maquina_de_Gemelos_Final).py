import time


class MaquinaGemelos:
    def __init__(self):
        #  Ajuste de Resistencia
        self.peso_minimo = int(input("Ingrese el peso mínimo (kg): "))
        self.peso_maximo = int(input("Ingrese el peso máximo (kg): "))
        self.peso_actual = self.peso_minimo

        #  Contador de Repeticiones
        self.repeticiones_actuales = 0
        self.repeticiones_objetivo = int(input("Ingrese el número objetivo de repeticiones: "))

        #  Tiempo de descanso
        self.tiempo_descanso_base = 60  # Tiempo de descanso base en segundos

    #  Metodo para ajustar la resistencia
    def ajustar_resistencia(self):
        peso = int(input(f"Elige un peso entre {self.peso_minimo} y {self.peso_maximo} kg: "))
        if self.peso_minimo <= peso <= self.peso_maximo:
            self.peso_actual = peso
            print(f"Resistencia ajustada a {self.peso_actual} kg.")
        else:
            print(f"Peso fuera de rango. Elige un valor entre {self.peso_minimo} y {self.peso_maximo} kg.")

    #  Metodo para contar repeticiones
    def contar_repeticion(self, movimiento_completo):
        if movimiento_completo:
            self.repeticiones_actuales += 1
            print(f"Repetición {self.repeticiones_actuales} completada.")
        else:
            print("Movimiento incompleto, no cuenta como repetición.")

    # Metodo para verificar el progreso
    def verificar_progreso(self):
        if self.repeticiones_actuales >= self.repeticiones_objetivo:
            print("Objetivo alcanzado.")
        else:
            print(
                f"Te faltan {self.repeticiones_objetivo - self.repeticiones_actuales} repeticiones para alcanzar el objetivo.")

    # Metodo para calcular el tiempo de descanso
    def calcular_tiempo_descanso(self):
        # Aumentar el tiempo de descanso en función de la carga y las repeticiones
        tiempo_descanso = self.tiempo_descanso_base + (self.repeticiones_actuales * self.peso_actual) / 100
        print(f"Tiempo de descanso calculado: {int(tiempo_descanso)} segundos.")
        return tiempo_descanso

    # Metodo para iniciar el descanso
    def iniciar_descanso(self):
        tiempo_descanso = self.calcular_tiempo_descanso()
        print(f"Descanso iniciado por {int(tiempo_descanso)} segundos.")
        time.sleep(tiempo_descanso)  # Simulación del descanso
        print("Descanso finalizado. Prepárate para la siguiente serie.")

    # Uso del metodo len para contar repeticiones
    def __len__(self):
        return self.repeticiones_actuales


# Ejemplo de uso
maquina = MaquinaGemelos()

# Ajustar resistencia
maquina.ajustar_resistencia()

# Breve simulación de movimientos del usuario con la maquina.
for i in range(12):
    maquina.contar_repeticion(i < 10)

# Verificar progreso
maquina.verificar_progreso()

# Acá usamos el metodo Len para contar las repeticiones totales.
print(f"Repeticiones totales completadas: {len(maquina)}")

# Iniciar el descanso
maquina.iniciar_descanso()
