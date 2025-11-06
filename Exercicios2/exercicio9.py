# 9. Validação de Dados (while): 
# ○ Peça ao usuário que digite um número entre 1 e 10. 
# ○ Use um while para garantir que a entrada seja válida. 
# ○ Se o número não estiver entre 1 e 10, imprima uma mensagem de erro e continue 
# pedindo até que a entrada seja correta. 

n = 0

while True: 
    n = int(input("Digite um numero entre 1 a 10: "))
    if n >= 1 and n <= 10:
        break
    else:
        print("Erro")
        