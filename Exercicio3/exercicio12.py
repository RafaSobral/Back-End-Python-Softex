# ; Exercício 12: Acumulador de Soma 
# ; ● Peça ao usuário para digitar 5 números. 
# ; ● Use um while com um contador para somar todos os números digitados e imprimir o 
# ; resultado final. 
i = 0 
soma = 0
while i < 5:
    n = int(input("Digite um numero: ")) 
    soma += n
    i += 1
print(soma)
