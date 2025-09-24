class Motor:
    def __init__(self, potencia):
        self.potencia = potencia


class CarroComMotor:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor(100)

    def exibir_potencia(self):
        print(f"O carro {self.modelo} tem {self.motor.potencia} cv de potência.")


carro_motor = CarroComMotor("Sedan")
carro_motor.exibir_potencia()

