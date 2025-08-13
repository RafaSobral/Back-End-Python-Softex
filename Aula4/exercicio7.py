# 7 - Verificação de número
# Peça algo ao usuário e use .isdigit() para verificar se ele
# digitou apenas números.

frase = input("Digite algo: ")

if frase.isdigit():
    print("Numero")
else:
    print("Tem letra ai jow")