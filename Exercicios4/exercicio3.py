# Exercício 3: Criando uma Lista com o Usuário 
# 1. Crie uma lista vazia chamada amigos. 
# 2. Crie uma variável chamada contador e defina seu valor inicial como 0. 
# 3. Use um loop while que continue rodando enquanto o contador for menor que 3. 
# 4. Dentro do loop, use o input() para pedir o nome de um amigo e guarde-o em uma 
# variável. 
# 5. Use o método .append() para adicionar o nome do amigo à lista amigos. 
# 6. Aumente o contador em 1 a cada volta do loop. 
# 7. Após o loop, use o print() para exibir a lista completa.

amigos = []

contador = 0 

while contador < 3:
    nome = input("Nome do amigo: ")
    amigos.append(nome)
    contador +=1
print(amigos)