class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

joao = Pessoa("João", 25)
maria = Pessoa("Maria", 30)

print(joao.nome, joao.idade)
print(maria.nome, maria.idade)

joao.apresentar()
maria.apresentar()
