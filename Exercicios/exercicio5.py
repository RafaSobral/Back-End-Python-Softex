# Nível Intermediário 
# Exercício 5: Crie um algoritmo que leia 5 números e, ao final, diga qual é o maior deles. Você 
# vai precisar de uma variável para guardar o maior número encontrado até o momento. 

i = 0 
maior = 0
while (i < 5):
    n = int(input(f"Digite o {i} numero: "))
    if i == 0 or n > maior:
        maior = n
    i += 1
print(f"O maior numero eh: {maior}" )
