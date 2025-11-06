# 5. Calculadora de Média (while e if): 
# ○ Crie um programa que peça notas ao usuário. 
# ○ Use um while para continuar pedindo notas até que o usuário digite -1. 
# ○ Ao final, calcule e imprima a média das notas. 

n = 0
s = 0
c = 0
while True:
    n = float(input("Digite uma nota: "))
    if n != -1:
        c += 1
        s += n
    elif n == -1:
        break

print(s / c)