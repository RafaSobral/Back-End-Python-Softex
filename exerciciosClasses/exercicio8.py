class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.nivel_combustivel = 0

    def abastecer(self, litros):
        self.nivel_combustivel += litros
        print(f"Carro abastecido. Nível atual: {self.nivel_combustivel} litros")

    def dirigir(self, distancia):
        consumo = distancia / 10  
        if consumo <= self.nivel_combustivel:
            self.nivel_combustivel -= consumo
            print(f"O carro andou {distancia} km. Combustível restante: {self.nivel_combustivel} litros")
        else:
            print("Não há combustível suficiente para a viagem.")


carro = Carro("Fusca")
carro.abastecer(10)
carro.dirigir(50)
carro.dirigir(100)