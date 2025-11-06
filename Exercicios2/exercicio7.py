# 7. Contador de Vogais (while): 
# ○ Peça ao usuário para digitar uma palavra. 
# ○ Use um loop while para percorrer a palavra (usando um índice). 
# ○ Conte quantas vogais (a, e, i, o, u) existem na palavra e imprima o total. 

p = input("Digite uma palavra: ")
i = 0
c = 0

# while (i < len(p)):
#     if p[i] == "a" or p[i] == "e" or p[i] == "i" or p[i] == "o" or p[i] == "u":
#         c += 1
#     i += 1
# print(c)


while (i < len(p)):
    if p[i].lower() in "aeiou":
        c += 1
    i += 1
print(c)
