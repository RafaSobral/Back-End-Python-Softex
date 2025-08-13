# 8 - Senha com validação de letras e números
# Peça uma senha e verifique com .isalnum() se ela contém
# apenas letras e números.

senha = input("Senha: ")

if senha.isalnum():
    print("Contem letras e numeros")
else:
    print("Não contem letras ou numeros")