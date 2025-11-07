# Exercício 15: Sorteando um Aluno para Apresentação 
# 1. Crie uma lista com pelo menos 5 nomes de alunos. 
# 2. Importe o módulo random. 
# 3. Use a função random.choice() para sortear um nome da lista. 
# 4. Exiba uma mensagem dizendo "O aluno sorteado para a apresentação é:" seguido do 
# nome do aluno.
import random

alunos = ["rafael","daniel","gabriel","samuel","miguel"]

print(random.choice(alunos))