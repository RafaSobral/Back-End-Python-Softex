# Exercício 9: Somando Elementos de uma Lista 
# 1. Crie uma lista de números. 
# 2. Crie uma variável chamada soma e defina seu valor inicial como 0. 
# 3. Use um loop for para percorrer cada número na lista. 
# 4. Dentro do loop, adicione o valor do número atual à variável soma. 
# 5. Após o loop, exiba o valor final da soma.

lista = [1,2,3,4,5,6]

soma = 0 

for n in lista:
    soma += n
print(soma)