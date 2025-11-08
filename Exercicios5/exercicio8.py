# Exercício 8 - Iniciante 
# Faça um programa que solicita uma palavra e imprime a quantidade de vogais (a, e, i, o, u) 
# que ela contém. 

palavra = input("Palavra: ")
soma = 0
for letra in palavra:
    if letra in "aeiou":
        soma +=1

print(f"Qtd vogal: {soma}")