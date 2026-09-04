import os
os.system("cls")

nota = int(input("Digite sua nota:"))

if nota >= 0 and nota <=10:
    print("Sua nota é", nota)
else:
    print("Sua nota deve estar entra 0 e 10")