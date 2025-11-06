# Nível Intermediário
# Exercício 8: Crie um algoritmo para calcular a tabuada de um número de 1 a 10. 
# Você vai precisar de um loop. 

n = int(input("Digite o numero que vc quer saber a tabuada: "))
i = 1
while(i < 10):
    print(f"{n} x {i} = {n*i}")
    i += 1