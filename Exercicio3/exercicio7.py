# ; Módulo 3: if-elif-else para Múltiplas Condições 
# ; Exercício 7: Classificador de Idade 
# ; ● Peça a idade de uma pessoa. 
# ; ● Use if-elif-else para classificar a idade em: 
# ; ○ "Criança" (0 a 12 anos) 
# ; ○ "Adolescente" (13 a 17 anos) 
# ; ○ "Adulto" (18 a 59 anos) 
# ; ○ "Idoso" (60 anos ou mais) 

i = int(input("Digite a sua idade: "))

if i >= 0 and i <= 12:
    print("Crianca")
elif i >= 13 and i <= 17:
    print("Adolescente")
elif i >= 18 and i <= 59:
    print("Adulto")
else:
    print("Idoso")