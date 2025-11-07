# ; Exercício 17: Sequência de Fibonacci 
# ; ● Peça um número n ao usuário. 
# ; ● Use um while para gerar e imprimir os primeiros n termos da sequência de Fibonacci (0, 
# ; 1, 1, 2, 3, 5, ...). 

n = int(input("Digite um numero: "))

i = 0
a, b = 0, 1 

while i < n:
    print(a)
    a, b = b , a + b
    i += 1 