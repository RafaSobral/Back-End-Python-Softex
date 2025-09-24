class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


caderno = Produto("Caderno", 15.50)
caneta = Produto("Caneta", 3.00)

print(caderno.nome, caderno.preco)
print(caneta.nome, caneta.preco)