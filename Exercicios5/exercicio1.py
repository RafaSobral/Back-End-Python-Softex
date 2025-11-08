# Exercício 1 - Iniciante 
# Crie um programa que pede ao usuário para digitar sua idade. Se a idade for maior ou igual a 
# 18, imprima "Você é maior de idade.". Caso contrário, imprima "Você é menor de idade.".

idade = int(input("Qual a sua idade: "))

if idade  >= 18:
    print("Voce eh maior de idade!")
else:
    print("Voce eh menor de idade")