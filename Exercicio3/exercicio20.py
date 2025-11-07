# ; Exercício 20: Jogo da Forca Simplificado 
# ; ● Defina uma palavra secreta em uma variável (str). 
# ; ● Use um while para dar ao usuário 5 chances de adivinhar a palavra. 
# ; ● A cada tentativa, o usuário digita uma letra. 
# ; ● Se a letra estiver na palavra, exiba as letras já descobertas (ex: _ y t _ _ n). 
# ; ● Se a letra não estiver, diminua as chances. 
# ; ● Se o usuário acertar todas as letras, imprima a palavra completa e uma mensagem de 
# ; vitória. Se as chances acabarem, imprima a palavra e uma mensagem de derrota.

palavra = "chaves"

c = 5

i = 0

letras = []

while True:
    print(f"Numero de chances: {c}")
    palpite = input("Qual a letra palpite ?")

    if palpite in palavra:
        print(f"Voce acertou uma letra! {palpite}")
        if palpite not in letras:
            letras.append(palpite)
    else:
        print("Letra errada")
        c -= 1

    exibicao = ""
    for letra in palavra:
        if letra in letras:
            exibicao += letra
        else:
            exibicao += "_"
    print(f"palavra: {exibicao}")

    if "_" not in exibicao:
        print("Parabens, voce venceu!")

    if c == 0:
        print("Suas tentativas acabaram!")
        break



