# ; Módulo 5: while com break e Validação de Dados 
# ; Exercício 13: Login com Tentativas 
# ; ● Defina uma senha secreta. 
# ; ● Use um while True e um contador de tentativas (máximo de 3). 
# ; ● Se o usuário acertar a senha, imprima "Login bem-sucedido!" e use break. 
# ; ● Se o usuário errar 3 vezes, imprima "Tentativas esgotadas!" e pare o programa.

senha = "12345"

i = 0

while True:
    p = input("Digite a senha: ")
    if p == senha:
        print("Login bem sucedido")
        break
    elif i == 2:
        print("Tentativas esgotadas")
        break
    i += 1
    