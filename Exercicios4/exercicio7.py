# Exercício 7: Adivinhe o Número 
# 1. Importe o módulo random. 
# 2. Use a função random.randint() para sortear um número entre 1 e 10 e guarde-o em uma 
# variável. 
# 3. Peça ao usuário para adivinhar o número usando o input() e guarde o palpite em uma 
# variável (lembre-se de converter para número com int()). 
# 4. Use uma estrutura if para verificar se o palpite do usuário é igual ao número sorteado. 
# 5. Exiba uma mensagem de "Parabéns!" se ele acertar, ou "Que pena!" se errar, informando 
# qual era o número correto. 

import random

random = random.randint(1,10)

p = int(input("Palpite: "))

if p == random:
    print("Voce acertou")
else:
    print(f"Voce errou, o numero era: {random}")