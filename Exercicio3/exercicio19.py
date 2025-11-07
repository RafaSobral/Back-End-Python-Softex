# ; Exercício 19: Caixa Eletrônico Simplificado 
# ; ● Defina um saldo inicial. 
# ; ● Use um while True para apresentar um menu ao usuário: 
# ; 1. Sacar 
# ; 2. Depositar 
# ; 3. Ver saldo 
# ; 4. Sair 
# ; ● Use if-elif-else para processar a escolha do usuário. 
# ; ○ Se sacar, verifique se há saldo suficiente. 
# ; ○ Se depositar, adicione o valor ao saldo. 
# ; ○ Se sair, use break. 
# ; ● Valide as entradas do usuário (por exemplo, não permitir saque de valor negativo).

saldo = 0

while True:
    print("Sacar (1)")
    print("Depositar (2)")
    print("Ver saldo (3)")
    print("Sair (4)")
    n = int(input("Digite a opcao desejada: "))
    if n == 1:
        if saldo > 0:
            print(f"Valor disponivel para saque {saldo}")
            saque = float(input("Quanto voce quer sacar ?"))
            if saque < 0:
                print("Digite um valor valido para saque")
            elif saque <= saldo:
                saldo -= saque
            elif saque > saldo:
                print("Voce nao pode sacar um valor maior que o saldo")
            
        else:
            print("Voce esta sem saldo para sacar")

    elif n == 2:
        print(f"Saldo atual: {saldo}")
        deposito = float(input("Digite o valor para depositar: "))
        if deposito < 0:
            print("Digite um valor valido")
        else:
            saldo += deposito

    elif n == 3:
        print(f"Saldo atual: {saldo}")

    elif n == 4:
        print("Obrigado por usar nossos servicos!")
        break
