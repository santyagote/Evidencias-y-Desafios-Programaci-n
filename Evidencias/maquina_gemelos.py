class MaquinaGemelos:
    def __init__(self, peso_minimo=20, peso_maximo=200, repeticiones_objetivo=10):
        self.peso_minimo = peso_minimo
        self.peso_maximo = peso_maximo
        self.peso_actual = self.peso_minimo
        self.repeticiones_actuales = 0
        self.repeticiones_objetivo = repeticiones_objetivo
        self.tiempo_descanso_base = 60  # Tiempo de descanso base en segundos

    #  Metodo para ajustar la resistencia
    def ajustar_resistencia(self, peso):
        if self.peso_minimo <= peso <= self.peso_maximo:
            self.peso_actual = peso
            return True
        else:
            return False

    #  Metodo para contar repeticiones
    def contar_repeticion(self, movimiento_completo):
        if movimiento_completo:
            self.repeticiones_actuales += 1
            return True
        else:
            return False

    # Metodo para verificar el progreso
    def verificar_progreso(self):
        return self.repeticiones_actuales >= self.repeticiones_objetivo

    # Metodo para calcular el tiempo de descanso
    def calcular_tiempo_descanso(self):
        tiempo_descanso = self.tiempo_descanso_base + (self.repeticiones_actuales * self.peso_actual) / 100
        return int(tiempo_descanso)

    # Metodo especial para obtener el número de repeticiones
    def __len__(self):
        return self.repeticiones_actuales
