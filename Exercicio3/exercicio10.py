# ; Módulo 4: Repetição com while Simples 
# ; Exercício 10: Contador Regressivo 
# ; ● Peça um número inteiro ao usuário. 
# ; ● Use um while para fazer uma contagem regressiva a partir desse número até 0. Imprima 
# ; cada número. 

n = int(input("Digite um numero inteiro: "))

while n > 0:
    n -= 1
    print(n)