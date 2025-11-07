# Exercício 14: Contando Ocorrências de uma Letra 
# 1. Peça ao usuário para digitar uma frase. 
# 2. Peça ao usuário para digitar uma letra. 
# 3. Crie uma variável contador_letras com o valor 0. 
# 4. Use um loop for para percorrer cada caractere da frase. 
# 5. Dentro do loop, use um if para verificar se o caractere atual é igual à letra que o usuário 
# digitou. Use o método .lower() para ignorar maiúsculas e minúsculas. 
# 6. Se for, adicione 1 à variável contador_letras. 
# 7. Ao final do loop, imprima quantas vezes a letra apareceu na frase.

frase = input("Digite uma frase: ")
letra = input("Digite uma letra: ")

contador_letras = 0 

for l in frase:
    if l == letra.lower():
        contador_letras += 1

print(f"Qtd de letras'{letra}': {contador_letras}")
