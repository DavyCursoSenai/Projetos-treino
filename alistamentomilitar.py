import os
os.system("cls")


print("SISTEMA MILITAr")
sexo = str(input("Digite seu sexo?"))
nascimento = int(input("Digite seu ano de nascimento?"))
idade = (2026 - nascimento)


if sexo == "Masculino" and idade >= 18:
    print("Deve se apresentar no exército brasileiro")
else:
    print("Não deve se apresentar no exército brasileiro")