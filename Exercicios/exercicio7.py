# Nível Intermediário
# Exercício 7: Crie um algoritmo para um sistema de login simples. Peça ao usuário que digite 
# um nome de usuário e uma senha. Se o usuário for "admin" e a senha for "12345", diga "Login 
# bem-sucedido". Caso contrário, diga "Login ou senha incorretos". 

nome = input("Digite um nome: ")
senha = input("Digite uma senha: ")

if nome == "admin" and senha == "12345":
    print("Login bem sucedido")
else:
    print("Login ou senha incorretos")