# Nível Básico
# Exercício 4: Crie um algoritmo que leia 3 notas de um aluno, calcule a média e diga 
# "Aprovado" se a média for maior ou igual a 7, ou "Reprovado" se for menor que 7. 

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")
else: 
    print("Reprovado")