import os
import sys
os.system("cls")

numero = int(input("Digite um número aleatório:"))

if numero >= 10 and numero <= 20:
    print(f"O número {numero} está dentro do intervalo")
else:
    print("SISTEMA FINALIZADO")
    sys.exit()
