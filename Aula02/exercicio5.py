idade = int(input("Digite a sua idade:"))

if idade >= 0 and idade <= 12:
    print("Voce é uma criança")
elif idade >= 13 and idade <=17:
    print("Voce é um adolescente")
elif idade >=18 and idade <= 120:
    print("Voce é um adulto")
else:
    print("Insira uma idade real")