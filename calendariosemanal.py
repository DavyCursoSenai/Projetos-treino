import os

os.system("cls")

print("=> CALENDÁRIO SEMANAL <=")

calendario = int(input("Digite um número de 1 a 7 referente a dias da semana:"))

if calendario == 1:
    print("Domingo")

if calendario == 2:
    print("Segunda")

if calendario == 3:
    print("Terça")

if calendario == 4:
    print("Quarta")

if calendario == 5:
    print("Quinta")

if calendario == 6:
    print("Sexta")

if calendario == 7:
    print("Sábado")

if calendario > 7:
    print("Data inválida")