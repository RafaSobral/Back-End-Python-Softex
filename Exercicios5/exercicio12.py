# Exercício 12 - Intermediário 
# Faça um programa que simula a entrada de um sistema. O programa deve pedir uma senha e 
# continuar pedindo até que a senha correta ("python123") seja digitada. Use um loop while e 
# break. 

senha = ""

while senha != "python123":
    senha = input("Senha: ")
print("Senha correta!")