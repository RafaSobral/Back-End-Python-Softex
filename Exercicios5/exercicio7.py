# Exercício 7 - Iniciante 
# Crie um programa que pede ao usuário para digitar um número e usa um loop for para 
# imprimir a tabuada desse número de 1 a 10.

n = int(input("Digite um numero: "))

for i in range(11):
    print(f"{n} x {i} = {n*i}")