# ; Exercício 8: Avaliador de Notas 
# ; ● Peça a nota de um aluno (float). 
# ; ● Use if-elif-else para atribuir um conceito: 
# ; ○ = 9.0: Conceito A 
# ; ○ = 7.0: Conceito B 
# ; ○ = 5.0: Conceito C 
# ; ○ < 5.0: Conceito D 

n = float(input("Digite a nota: "))
if n == 9.0:
    print("Conceito A")
elif n == 7.0:
    print("Conceito B")
elif n == 5.0:
    print("Conceito C")
elif n < 5.0:
    print("Conceito D")