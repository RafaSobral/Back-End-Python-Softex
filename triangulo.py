

print("Desafio do Triangulo: Vamos descobrir se os três números que você escolheu conseguem formar um triangulo?")

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






