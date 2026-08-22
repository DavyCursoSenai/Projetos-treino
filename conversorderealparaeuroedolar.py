import os

os.system("cls")

moeda_brl = float(input("Digite o valor em real: "))

euro = moeda_brl * 0.17
dolar = moeda_brl * 0.19
peso_argentino = moeda_brl * 291.59

print("Euro: ", euro)
print("Dólar: ", dolar)
print("Peso Argentino: ", peso_argentino)

