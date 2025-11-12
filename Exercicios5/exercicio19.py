# Exercício 19 - Intermediário 
# Faça um programa que pede ao usuário para digitar 5 números. O programa deve somar 
# apenas os números que são positivos. Use um loop for.

i = 0
soma = 0

for i in range(5):
    n = int(input("Digite o primeiro numero: "))
    if n >= 0:
        soma += n

print(soma)
