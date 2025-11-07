# ; Exercício 15: Validação de E-mail 
# ; ● Use um while True para pedir um e-mail ao usuário. 
# ; ● Verifique se o e-mail contém o caractere @. 
# ; ● Se contiver, imprima "E-mail válido" e use break. 
# ; ● Se não contiver, imprima "E-mail inválido. Digite novamente."

while True:
    e = input("Digite seu email: ")
    if "@" in e:
        print("E-mail valido")
        break
    print("E-mail invalido, digite novamente")