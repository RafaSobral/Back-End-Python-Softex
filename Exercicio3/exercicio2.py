# ; Exercício 2: Calculadora de Desconto 
# ; ● Peça ao usuário para digitar o preço original de um produto (float). 
# ; ● Se o preço for maior que R$ 100,00, aplique um desconto de 10% e imprima o novo 
# ; preço. 

p = float(input("Digite o preco do produto: "))
desconto = 0.10

if p > 100.00:
    p_final = p * (1 - desconto)

print(p_final)