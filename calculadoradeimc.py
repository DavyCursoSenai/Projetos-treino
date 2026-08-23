import os

os.system("cls")

print("=> CALCULADORA IMC <=")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = float 

imc = peso / (altura * altura) 


print("=> SEU IMC <=")

print("Imc = ", imc)

if imc < 18.5:
    print("Magreza")

if imc >= 18.5 and 24.9:
    print("Peso normal")

if imc >= 25.0 and 29.9:
    print("Sobrepeso")

if imc >= 30.0 and 34.9:
    print("Obesidade grau I")

if imc >= 35.0 and 39.9:
    print("Obesidade grau II")

if imc > 40.0:
    print("Obesidade grave")
