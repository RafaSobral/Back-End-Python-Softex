# 8. Jogo de Adivinhação Melhorado (while, if-elif-else e break): 
# ○ Defina um número secreto. 
# ○ Use um loop while com um contador de tentativas, limitando a 3 tentativas. 
# ○ A cada tentativa, diga se o palpite é maior ou menor que o número secreto. 
# ○ Se o usuário acertar, imprima "Parabéns, você acertou!" e use break. 
# ○ Se as 3 tentativas acabarem, imprima "Você perdeu. O número era [número 
# secreto]." 

import random

n = random.randint(0,100)
i = 0
p = 0
# acertou = False

while(i < 3):
    print(n)
    p = int(input("Digite seu palpite: "))
    if p > n:
        print("palpite maior que o numero")
    elif p < n:
        print("Palpite menor que o numero")
    else:
        print("Parabens, voce acertou!")
        # acertou = True
        break
    i += 1

else:
    print(f"Voce perdeu, o numero era {n}")

# if not acertou:   
#     print(f"Voce perdeu, o numero era {n}")
    


    