import os
os.system("cls")

while True:
    print("1 - CADASTRO")
    print("2 - LOGIN")
    print("0 - FINALIZAR")

    escolha = input("Escolha uma opção:")

    if escolha == '1':
        nomec = str(input("Digite seu nome:"))
        senhac = input("Digite sua senha:")

        print(f"{nomec} foi cadastrado com sucesso!!")

    if escolha == '2':
        nomel = str(input("Digite o nome cadastrado:"))
        senhal = input("Digite a senha cadastrada:")

        if nomel == nomec and senhal == senhac:
            print("Você está logado")
        else:   
            print("Você não tem cadastro")
    if escolha == '0':
        print("Sistema finalizado")
        break




