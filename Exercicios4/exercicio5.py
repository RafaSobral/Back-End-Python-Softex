# Exercício 5: Números Pares com range() 
# 1. Use um loop for e a função range() para gerar os números pares de 2 até 10. 
# 2. Dentro do loop, use o print() para exibir cada número. 

for n in range(1,11):
    if n % 2 == 0:
        print(n)    

for n in range(2,11,2):
    print(n)