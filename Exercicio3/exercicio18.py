# ; Exercício 18: Calculadora de Fatorial 
# ; ● Peça um número n ao usuário. 
# ; ● Use um while para calcular o fatorial de n (por exemplo, 5! = 5 * 4 * 3 * 2 * 1). 
# ; ● Imprima o resultado. 

n = int(input("Digite um numero: "))

fatorial = 1

i = n


while i > 0: 
    fatorial *= i
    i -= 1

print(fatorial)

