# 4. Sistema de Login Básico (while e break): 
# ○ Defina um nome de usuário e uma senha corretos (ex: admin, 1234). 
# ○ Use um loop while True para pedir ao usuário que digite o nome de usuário e a 
# senha. 
# ○ Se ambos estiverem corretos, imprima "Login bem-sucedido!" e use break para 
# sair do loop. 
# ○ Se estiverem incorretos, imprima "Login inválido. Tente novamente."


n = 0
s = 0

while(n != "admin" or s != "1234"):
    n = input("Digite o seu nome: ")
    s = input("Digite a sua senha: ")
    if n == "admin" and s == "1234": 
        print("Login bem-sucedido")
        break
    print("Login invalido, tente novamente")