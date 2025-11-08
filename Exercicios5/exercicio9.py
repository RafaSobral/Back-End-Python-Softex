# Exercício 9 - Iniciante 
# Escreva um programa que solicita a senha do usuário. A senha deve ter no mínimo 6 
# caracteres. Se não tiver, imprima uma mensagem de erro.

senha = input("Senha: ")

if len(senha) < 6:
    print("Erro")
else:
    print("Senha cadastrada")