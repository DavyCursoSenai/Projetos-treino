import os

os.system("cls")

print("=-> APROVADOR DE NOTAS <-=")

nota = int(input("Digite sua nota:"))

print("\n VOCÊ ESTÁ...")

if nota >= 6:
    print("\n ->Aprovado <- ")
    print("\n PARABÉNS")
elif nota <= 4:
    print("\n -> Reprovado <- ")
    print("\n EITA")
elif nota == 5:
    print("\n -> Recuperação <-")
    print("\n BOA SORTE")



