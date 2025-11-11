# Exercício 14 - Intermediário 
# Faça um programa que solicita um número inteiro e calcula o seu fatorial (ex: 5! = 120). Use 
# um loop for.

n = int(input("Digite um numero inteiro: "))

fatorial = 1

for i in range(1, n + 1):
    fatorial *= i
    print(fatorial)
            