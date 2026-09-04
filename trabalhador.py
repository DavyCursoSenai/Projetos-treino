import os
os.system("cls")

matricula = int(input("Digite sua matrícula:"))
ano_de_nascimento = int(input("Digite seu ano de nascimento:"))
tempo_de_trabalho = int(input("Digite o tempo de trabalho:"))
idade = (2026 - ano_de_nascimento)

os.system("cls")

print("Matrícula:", matricula)
print("Idade:", idade)
print("Tempo de trabalho:", tempo_de_trabalho)



if idade >= 65 or tempo_de_trabalho >= 30:
    print("Requerer aposentadoria")
else:
    print("Não requerer aposentadoria")