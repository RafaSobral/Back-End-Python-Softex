# Exercício 13: Verificador de Palíndromo 
# 1. Peça ao usuário para digitar uma palavra. 
# 2. Use o método .lower() para converter a palavra para minúsculas, garantindo que "Arara" 
# e "arara" sejam tratadas da mesma forma. 
# 3. Crie uma nova variável para guardar a palavra reversa. Uma forma simples é usar 
# fatiamento de string: palavra[::-1]. 
# 4. Use uma estrutura if para comparar a palavra original com a palavra reversa. 
# 5. Exiba se a palavra é ou não um palíndromo (uma palavra que se lê da mesma forma de 
# trás para frente). 


palavra = input("Digite uma palavra: ").lower()

reversa = palavra[::-1]

if palavra == reversa:
    print("Eh palindromo")
else:
    print("Nao eh palindromo")

