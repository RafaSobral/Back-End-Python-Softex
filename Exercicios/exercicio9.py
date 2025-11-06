# Nível Avançado 
# Exercício 9: Crie um algoritmo para simular uma votação. Peça que as pessoas votem em 
# "Candidato A", "Candidato B" ou "Branco". A votação termina quando o usuário digitar "Fim". 
# Ao final, mostre o total de votos para cada candidato e o total de votos brancos. 

r = 0 
ca = 0
cb = 0
vb = 0
while(r != "fim"):
    print("Em quem voce quer votar: ")
    print("Candidato (A)")
    print("Candidato (B)")
    print("Branco")
    r = input("Voto: ")
    if r == "a":
        ca += 1

    if r == "b":
        cb += 1

    if r == "branco":
        vb += 1

    if r == "fim":
        break

print(ca)
print(cb)
print(vb)