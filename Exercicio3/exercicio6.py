# ; Exercício 6: Verificador de Par ou Ímpar 
# ; ● Peça ao usuário um número inteiro. 
# ; ● Use o operador de módulo (%) e uma estrutura if-else para determinar e imprimir se o 
# ; número é "par" ou "ímpar".   

n = int(input("Digite um numero inteiro: "))
if n % 2 == 0:
    print("O numero eh par")
else:
    print("O numero eh impar")