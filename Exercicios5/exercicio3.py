# Exercício 3 - Iniciante 
# Escreva um programa que pede ao usuário para digitar uma cor. O programa deve verificar se 
# a cor é "vermelho", "azul" ou "amarelo" e imprimir "Cor primária!" se a condição for 
# verdadeira. 

cor = input("Digite uma cor: ").lower()
cores = ["vermelho", "azul", "amarelo"]

if cor in cores:
    print("Cor primaria!")