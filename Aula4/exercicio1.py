# 1 - Comparando nomes ignorando maiúsculas
# Peça dois nomes e verifique se são iguais usando .lower().
# Se forem iguais, mostre "Nomes iguais", senão "Nomes diferentes".

nome1 = input("Digite o primeiro nome: ").lower()
nome2 = input("Digite o segundo nome: ").lower()

if nome1 == nome2:
    print("Os nomes são iguais")
else: 
    print("Os nomes são diferentes")