# Nível Avançado
# Exercício 10: Crie um algoritmo para um jogo de adivinhação. O programa "pensa" em um 
# número secreto entre 1 e 100. O usuário tenta adivinhar. O programa diz se o palpite é maior 
# ou menor que o número secreto. O jogo termina quando o usuário acertar o número. Ao final, 
# diga quantas tentativas foram necessárias. 

import random 

nAleatorio = random.randint(1,100)

p = 0
t = 0

while(nAleatorio != p):
    p = int(input("Digite o seu palpite: "))

    if nAleatorio > p:
        print("O palpite eh menor que o numero")
        t += 1
    elif nAleatorio < p:
        print("O palpite eh maior que o numero")
        t += 1
    else:
        print("Voce acertou!!")
        print(f"numero de tentativas: {t}")
        break