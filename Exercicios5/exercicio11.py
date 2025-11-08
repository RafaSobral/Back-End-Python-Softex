# Exercício 11 - Intermediário 
# Crie um programa que solicita ao usuário um número e, em seguida, usa um loop for para 
# imprimir todos os números pares de 2 até o número digitado.

n = int(input("Digite um numero: "))

for i in range(2,n + 1):
    if i % 2 == 0:
        print(i)