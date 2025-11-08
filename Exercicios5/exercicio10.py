 # Exercício 10 - Iniciante 
# Crie um programa que simula um login. Ele deve pedir um nome de usuário (admin) e uma 
# senha (senha123). O programa deve permitir apenas uma tentativa.

usuario = input("Usuario: ")
senha = input("Senha: ")

if usuario == "admin" and senha == "senha123":
    print("Login bem-sucedido")
else:
    print("Usuario ou senha invalidos")