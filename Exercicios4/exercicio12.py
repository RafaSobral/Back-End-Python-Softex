# Exercício 12: Sistema de Login com Tentativas 
# 1. Defina um nome de usuário e uma senha corretos em variáveis. 
# 2. Crie uma variável tentativas com o valor inicial de 3. 
# 3. Use um loop while que continue enquanto o número de tentativas for maior que 0. 
# 4. Dentro do loop, peça o nome de usuário e a senha. 
# 5. Use uma estrutura if para verificar se o login está correto. Se sim, imprima "Login 
# bem-sucedido!" e use o comando break para sair do loop. 
# 6. Se o login estiver incorreto, imprima "Usuário ou senha incorretos." e diminua a variável 
# tentativas em 1. 
# 7. Após o loop, use o if para verificar se as tentativas chegaram a 0. Se sim, imprima "Você 
# excedeu o número de tentativas.". 

usuario = "rafael"
senha = "12345"

i = 3

while i > 0:
    nome = input("Nome: ")
    password = input("Pass: ")
    if nome == usuario and senha == password:
        print("Login bem-sucedido")
        break
    
    print("Usuario ou senha incorretos")
    i -= 1

if i == 0:
    print("Voce excedeu o numero de tentativas")