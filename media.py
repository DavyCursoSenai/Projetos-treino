import os
os.system("cls")

media = float(input("Digite sua média:"))
faltas = int(input("Digite seu número de faltas:"))

if media >= 7.0 and faltas <= 40:
    print("Você está aprovado")
else:
    print("Você está reprovado")