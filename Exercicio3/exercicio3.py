# ; Exercício 3: Verificador de Divisibilidade 
# ; ● Peça ao usuário um número inteiro. 
# ; ● Verifique se o número é divisível por 5 (use o operador %). 
# ; ● Se for, imprima "O número é divisível por 5". 

n = int(input("digite um numero inteiro: "))
if n % 5 == 0:
    print("O numero eh divisivel por 5")