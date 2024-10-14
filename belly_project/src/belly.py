# src/belly.py
class Belly:
    def __init__(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        # Ahora permitimos grandes cantidades, como 1000 pepinos
        if pepinos <= 0:
            raise ValueError("La cantidad de pepinos debe ser positiva.")
        #if pepinos > 100:
        #    raise ValueError("No puedes comer más de 100 pepinos a la vez.")
        self.pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        if tiempo_en_horas > 0:
            self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        return self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10

    def pepinos_restantes(self, total_pepinos):
        if total_pepinos < self.pepinos_comidos:
            raise ValueError("No se pueden comer más pepinos de los disponibles.")
        return total_pepinos - self.pepinos_comidos
