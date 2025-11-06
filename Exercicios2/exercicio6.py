# 6. Classificador de Triângulos (if-elif-else): 
# ○ Peça ao usuário para digitar o comprimento de três lados de um triângulo. 
# ○ Use a lógica condicional para classificar o triângulo em: 
# ■ "Equilátero" (todos os lados iguais) 
# ■ "Isósceles" (dois lados iguais) 
# ■ "Escaleno" (todos os lados diferentes) 

l1 = float(input("Digite o primeiro lado: "))
l2 = float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceiro lado: "))

if l1 == l2 and l2 == l3: 
    print("Equilatero, todos os lado iguais!")
elif l1 == l2 or l2 == l3 or l3 == l1:
    print("Isosceles, dois lados iguais")
else:
    print("Escaleno, todos os lados diferentes")