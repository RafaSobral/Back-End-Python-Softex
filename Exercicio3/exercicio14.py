# ; Exercício 14: Somador de Números Positivos 
# ; ● Use um while True para pedir números ao usuário. 
# ; ● Some todos os números positivos. 
# ; ● Se o usuário digitar um número negativo, use break para sair do loop e imprima a soma 
# ; total.
 
soma= 0 

while True:
    n = int(input("Digite um numero: "))
    if n < 0:
        break
    soma += n
print(soma)