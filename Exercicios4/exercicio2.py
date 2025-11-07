# Exercício 2: Contando Caracteres de uma Palavra 
# 1. Use o input() para pedir ao usuário que digite uma palavra e guarde-a em uma variável 
# chamada palavra. 
# 2. Use a função len() para contar o número de caracteres da palavra. Guarde o resultado 
# em uma variável chamada tamanho. 
# 3. Use o print() para exibir uma mensagem informando o tamanho da palavra. 

palavra = input("Digite uma palavra: ")

tamanho = len(palavra)

print(f"A palavra '{palavra}' tem o tamanho de {tamanho} letras")