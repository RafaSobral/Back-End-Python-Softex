# Exercício 18 - Intermediário 
# Crie um programa que solicita uma string e inverte a ordem de seus caracteres. Por exemplo, 
# "python" se torna "nohtyp". 

palavra = input("Digite uma palavra: ")

string = ""

for letra in range(len(palavra) -1, -1, -1):
    string += palavra[letra]

print(string)
