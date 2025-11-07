# Exercício 6: Imprimindo uma Lista de Trás para Frente 
# 1. Crie uma lista com 5 números inteiros. 
# 2. Use um loop for e a função range() para percorrer os índices da lista de trás para frente. 
# 3. Dentro do loop, use o print() para exibir o número correspondente a cada índice. 

numeros = [1,2,3,4,5]

for n in range(len(numeros) -1, -1, -1):
    print(n)
    