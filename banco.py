import os
import sys 
os.system('cls')

1 == (print("Deposito - 1"))
2 == print("Saque - 2")
3 == print("Pix - 3")
0 == print("Sair - 0")

escolha = int(input("O que desejas:"))


if escolha == 1:
    deposito = input("Quanto você quer depositar:")
    print("Você depositou", "R$",deposito, "com sucesso!!")
elif escolha == 2:
    saque = input("Quanto você deseja sacar:")
    print("Você sacou","R$", saque, "com sucesso")

if escolha == 3:
    pix = str(input("Para quem deseja enviar:"))
    valor = int(input(f"Quanto desejas enviar para {pix}:"))
    os.system("cls")
    1 == print("1 - SIM")
    2 == print("2 - NÃO")

confirmacao = int(input(f"Você deseja enviar R$ {valor} para {pix}:"))

if confirmacao == 1:
    print("Transação confirmada com sucesso")
elif confirmacao == 2:
    print("Transação cancelada")


elif escolha == 0:
    print("PROGRAMA FINALIZADO")
    sys.exit()
else:
   print ("opção invalida")


