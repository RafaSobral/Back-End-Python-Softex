# ; Exercício 11: Tabuada Simples 
# ; ● Peça um número ao usuário. 
# ; ● Use um while para imprimir a tabuada desse número, de 1 a 10. 
# ; ○ Exemplo: 5 x 1 = 5, 5 x 2 = 10, etc.

n = int(input("Digite um numero: "))
i = 1

while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1