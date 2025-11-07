# Exercício 11: Capitalizando Nomes em uma Lista 
# 1. Crie uma lista com 3 nomes, todos em letras minúsculas (ex: ['joão', 'maria', 'pedro']). 
# 2. Crie uma nova lista vazia chamada nomes_formatados. 
# 3. Use um loop for para percorrer a primeira lista. 
# 4. Dentro do loop, use o método .capitalize() em cada nome. 
# 5. Use o método .append() para adicionar o nome formatado à nova lista. 
# 6. Ao final, imprima a lista nomes_formatados. 

nomes = ["rafael", "gabriel", "daniel"]
nomes_formatados = []

for nome in nomes:
    nomes_formatados.append(nome.capitalize())

print(nomes_formatados)