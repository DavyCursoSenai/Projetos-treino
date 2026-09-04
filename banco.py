import os
os.system("cls")

saldo = 0.0

while True :
    print("1 - Deposito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Pix")
    print("0 - Sair")


    escolha = input("Escolha uma opção:")

    if escolha == "1":
        valor = float(input("Quanto deseja depositar?"))
        print(f"Você deseja depositar R$ {valor:.2f} na sua conta?")
        print("1 - SIM")
        print("2 - NÃO")


        confirmacao = input("Escolha:")

        if confirmacao == "1":
            saldo += valor
            print(f"R$ {valor:.2f} foi depositado com sucesso!")
        else:
            print(f"R$ {valor:.2f} não foi depositado")


    if escolha == "2":
        valor = float(input("Quanto deseja sacar?"))

        if valor > saldo:
              print("Saldo Indisponivel")
        else:

            print(f"Você deseja sacar R$ {valor:.2f} na sua conta?")
            print("1 - SIM")
            print("2 - NÃO")

            confirmacao = input("Escolha:")

            if confirmacao == "1":
                saldo -= valor
                print(f"R$ {valor:.2f} foi sacado com sucesso!")
            else:
                print(f"R$ {valor:.2f} não foi sacado")

   
    if escolha == "3":
        print(f"O seu saldo atual => R$ {saldo:.2f}")

    if escolha == "4":
       destino = str(input("Para quem voce quer enviar ->"))
       pix = float(input("Quanto voce quer mandar?"))

       if pix > saldo:
           print("Valor indisponivel")
       else:
           print(f"Voce quer mandar R$ {pix:.2f} para {destino}?")
           print("1 - SIM")
           print("2 - NÃO")
           confirmacaop = input("Escolha")

           if confirmacaop == "1":
               print(f"Pix para {destino} enviado com sucesso!")
               saldo -= pix
           elif confirmacaop == "2":
               print(f"Pix para {destino} cancelado")
               

    if escolha == "0":
        print("Sistema encerrado")

        break
          