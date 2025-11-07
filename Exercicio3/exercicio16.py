# ; Módulo 6: Desafios Combinados e Lógica Avançada 
# ; Exercício 16: Jogo de Adivinhação com Dicas 
# ; ● Defina um número secreto. 
# ; ● Use um while True e um contador de tentativas. 
# ; ● A cada tentativa, diga se o palpite é "maior" ou "menor" que o número secreto. 
# ; ● Quando o usuário acertar, imprima a mensagem de vitória e quantas tentativas foram 
# ; necessárias. 

secret_number = 23
i = 0

while True:
    p = int(input("Palpite: "))
    if p > secret_number:
        print("O palpite eh maior")
    elif p < secret_number:
        print("O palpit eh menor")
    else:
        print(f"Voce acertou! N  de tentativas: {i}")
        break
    i += 1