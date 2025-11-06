# Par ou Ímpar (Operadores e if-else): 
# ○ Peça ao usuário para digitar um número inteiro. 
# ○ Use o operador de módulo (%) para verificar se o número é par (o resto da 
# divisão por 2 é 0). 
# ○ Imprima se o número é "Par" ou "Ímpar". 

n = int(input("Digite um numero: "))

if n % 2 == 0:
    print("Par")
else:
    print("Impar")