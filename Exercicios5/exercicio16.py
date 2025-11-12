# Exercício 16 - Intermediário 
# Escreva um programa que pede ao usuário para digitar uma frase e conta quantas palavras 
# ela tem. Use um loop for para percorrer a string. 

palavra = input("Digite uma palavra: ")

contador = 1

for letra in palavra:
    if letra == " ":
        contador +=1

print(f"Qtd de palavras: {contador}")
