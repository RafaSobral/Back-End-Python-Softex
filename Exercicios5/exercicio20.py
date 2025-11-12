# Exercício 20 - Intermediário 
# Escreva um programa que pede ao usuário para digitar um nome e um sobrenome. O 
# programa deve imprimir o nome completo e a quantidade de caracteres em cada um, 
# separadamente. 

nome = input("Digite seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")

nome_completo  = ""

nome_completo = nome + " " + sobrenome

print(nome_completo)

print(len(nome))

print(len(sobrenome))