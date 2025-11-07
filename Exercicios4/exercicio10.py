# Exercício 10: Validando uma Senha Simples 
# 1. Crie duas variáveis, usuario_original e senha_original, com valores pré-definidos. 
# 2. Peça ao usuário para digitar um nome de usuário e uma senha. 
# 3. Use uma estrutura if com a condição e (and) para verificar se o nome de usuário E a 
# senha estão corretos. 
# 4. Exiba uma mensagem de sucesso ou erro. 

usuario_original = "admin"
senha_original = "12345"

login = input("Digite o login: ")
senha = input("Digite a senha: ")

if login == "admin" and senha == "12345":
    print("Login bem sucedido")
else:
    print("Login ou senha invalidos")