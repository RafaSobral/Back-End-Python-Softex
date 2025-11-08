# Exercício 13 - Intermediário 
# Escreva um programa que pede ao usuário para digitar uma frase e, em seguida, remove 
# todos os espaços em branco, imprimindo a frase modificada e o seu novo comprimento.

frase = input("Digite uma frase: ")

nova_frase = ""

for posicao in frase:
    if posicao != " ":
        nova_frase += posicao
print(nova_frase,len(nova_frase))

# com replace

nova_frase = frase.replace(" ","")

print(nova_frase)
