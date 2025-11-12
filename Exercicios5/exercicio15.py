# Exercício 15 - Intermediário 
# Crie um programa que solicita ao usuário um número e, em seguida, usa um loop while para 
# calcular a soma de todos os números de 1 até o número digitado.

n = int(input("Digite um numero: "))

soma = 0

i = 0 

while i <= n:
    soma += i 
    i += 1

print(soma)