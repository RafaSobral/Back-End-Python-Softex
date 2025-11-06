# Maior de Idade (Aninhamento de if): 
# ○ Peça ao usuário o nome e a idade. 
# ○ Se a idade for maior ou igual a 18, imprima: "Olá, [nome]! Você é maior de idade." 
# ○ Se for menor, imprima: "Olá, [nome]! Você é menor de idade." 

n = input("Digite o seu nome: ")
i = int(input("Digite a sua idade: "))

if i >= 18:
    print(f"Ola {n}, voce eh maior de idade")
else:
    print(f"ola {n}, voce eh menor de idade")