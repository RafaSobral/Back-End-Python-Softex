'''Seu objetivo: Escrever um algoritmo em Python que determine se três valores, 
fornecidos pelo usuário, podem formar um triângulo.

As Regras do Jogo
1- Teste se a entrada de dados é um número.
2- Se for um número teste se é positivo
3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas condições importantes:

A soma: A soma de quaisquer dois lados deve ser maior que o terceiro lado.

lA<lB+lC

lB<lA+lC

lC<lA+lB

A diferença: O valor absoluto da diferença entre dois lados deve ser menor que o terceiro lado.

lA>∣lB−lC∣

lB>∣lA−lC∣

lC>∣lA−lB∣

Dica: use o método abs() para ter o valor absoluto de um número.
quero que vc me ajude a resolveer esse desafio'''

print("Desafio do Triangulo: Vamos descobrir se os três números que você escolheu conseguem formar um triangulo?")

'''while True:
    ladoA = int(input("Digite o 1° número: "))
    if ladoA <= 0:
        print("Invalido digite um número inteiro!")
        continue
    ladoB = int(input("Digite o 2° número: "))
    if ladoB <= 0:
      print("Invalido digite um número inteiro!")
      continue
    ladoC = int(input("Digite o 3° númeoro: "))
    if ladoC <= 0:
        print("Invalido digite um número inteiro!")
        break
while True:
    soma = (ladoA < ladoB + ladoC) and (ladoB < ladoA + ladoC) and (ladoC < ladoA + ladoB)

    diferenca = (ladoA > abs(lB - lC)) and (lB > abs(lA - lC)) and (lC > abs(lA - lB))

    if soma and diferenca:
            print("Os valores podem formar um triângulo!")
    else:
        print("Entrada inválida! Digite apenas números.")'''

n1 = input("Digite o primeiro valor: ")
n2 = input("Digite o segundo valor: ")
n3 = input("Digite o terceiro valor: ")

if n1.isnumeric() and n2.isnumeric() and n3.isnumeric(): 
    a = int(n1)
    b = int(n2)
    c = int(n3)
    if a >= 0 and b >= 0 and c >= 0:
        soma = (a < b + c) and (b < a + c) and (c < a + b)
        diferenca = (a > abs(b - c)) and (b > abs(a - c)) and (c > abs(a - b))
        if soma and diferenca:
                print("Os valores podem formar um triângulo!")
        else:
            print("Entrada inválida! Digite apenas números.")
    else:
        print("Um dos numeros nao eh positivo")
else:
    print("Um dos valores digitados nao eh um numero!")





