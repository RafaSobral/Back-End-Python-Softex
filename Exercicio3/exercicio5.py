# ; Exercício 5: Maior de Dois Números 
# ; ● Peça ao usuário para digitar dois números inteiros. 
# ; ● Use if-else para descobrir qual dos dois é o maior e imprima o resultado.

n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))

if n1 > n2:
    print(f"O numero {n1} eh maior")
else:
    print(f"o numero {n2} eh maior")