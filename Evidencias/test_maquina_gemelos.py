import pytest
from maquina_gemelos import MaquinaGemelos


#  Prueba para el ajuste de resistencia
def test_ajustar_resistencia():
    maquina = MaquinaGemelos(peso_minimo=30, peso_maximo=150)

    # Probar peso dentro del rango
    assert maquina.ajustar_resistencia(50) == True
    assert maquina.peso_actual == 50

    # Probar peso fuera del rango
    assert maquina.ajustar_resistencia(200) == False
    assert maquina.peso_actual == 50  # El peso no debería cambiar


#  Prueba para contar repeticiones
def test_contar_repeticiones():
    maquina = MaquinaGemelos(repeticiones_objetivo=5)

    # Probar con movimientos completos
    for _ in range(3):
        assert maquina.contar_repeticion(True) == True
    assert len(maquina) == 3

    # Probar con un movimiento incompleto
    assert maquina.contar_repeticion(False) == False
    assert len(maquina) == 3  # El contador no debería cambiar


#  Prueba para verificar progreso
def test_verificar_progreso():
    maquina = MaquinaGemelos(repeticiones_objetivo=5)

    # Añadir repeticiones
    for _ in range(5):
        maquina.contar_repeticion(True)

    # Comprobar si se alcanza el objetivo
    assert maquina.verificar_progreso() == True


#  Prueba para calcular el tiempo de descanso
def test_calcular_tiempo_descanso():
    maquina = MaquinaGemelos(peso_minimo=30, peso_maximo=150)

    # Ajustar resistencia y añadir repeticiones
    maquina.ajustar_resistencia(60)
    for _ in range(4):
        maquina.contar_repeticion(True)

    # Calcular el tiempo de descanso
    assert maquina.calcular_tiempo_descanso() == 62  # 60 + (4 * 60 / 100)
