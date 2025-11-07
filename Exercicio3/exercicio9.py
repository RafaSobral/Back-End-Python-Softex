# ; Exercício 9: Categoria de CNH 
# ; ● Peça a idade e se o usuário tem CNH (True ou False). 
# ; ● Use if-elif-else com operadores lógicos (and e or) para: 
# ; ○ Se for maior de 18 e tiver CNH: "Pode dirigir." 
# ; ○ Se for maior de 18 e não tiver CNH: "Precisa tirar a CNH." 
# ; ○ Se for menor de 18: "Não pode dirigir."

i = int(input("Digite a sua idade: "))
c = input("Voce tem CNH ?")

b = c.lower() == "true"

if i >= 18 and b:
    print("Pode dirigir")
elif i >= 18 and not b: 
    print("Vamo querer tirar essa carteira ai")
else:
    print("Pode nao man kkkk")