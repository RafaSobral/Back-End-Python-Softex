# 10. Calculadora de Média com Repetições (while, if-else e break): 
# ○ Crie um programa que permita ao usuário calcular a média de uma turma. 
# ○ Peça a quantidade de alunos. Use um while para garantir que o número seja 
# positivo. 
# ○ Em seguida, use outro while para pedir as notas de cada aluno (uma por uma). 
# ○ Calcule a média final da turma.

qtd_aluno = 0
i = 0
soma = 0

while True:
    qtd_aluno = int(input("Digite a quantidade de alunos: "))
    if qtd_aluno >= 1:
        break
    else:
        print("O numero de alunos deve ser positivo")

while(i < qtd_aluno):
    nota = float(input("Digite a nota: "))
    soma += nota 
    i += 1

print(soma / qtd_aluno )
