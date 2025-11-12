# Exercício 17 - Intermediário 
# Faça um programa que simula um quiz simples. Pergunte qual é a capital do Brasil. O 
# programa deve continuar pedindo a resposta até que o usuário acerte, usando um loop while 
# e break. 



while True:
    resposta = input("Qual a capital do Brasil ?").lower()
    if resposta == "brasilia":
        print("Voce acertou!")
        break