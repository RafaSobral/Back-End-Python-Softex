# Nível Básico 
# Exercício 1: Crie um algoritmo que leia a idade de uma pessoa e diga "Você é adulto" se a 
# idade for 18 ou mais, ou "Você é menor de idade" se for menos que 18.

idade = int(input("Digite a sua idade: "))
if idade >= 18:
    print("Voce eh um adulto")
else:
    print("Voce eh menor de idade")