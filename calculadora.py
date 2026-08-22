import os

os.system("cls")

print("=> CALCULADORA <=")

primeiro_numero = int(input("Digite o primeiro número:"))
segundo_numero = int(input("Digite o segundo número:"))

soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

print("=> RESULTADOS <=")

print("Soma =", soma)
print("Subtração =", subtracao)
print("Multiplicação =", multiplicacao)
print("Divisão =", divisao)