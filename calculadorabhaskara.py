
import os

os.system("cls")

print("\n => Calculadora de Bhaskara <=")

a = int(input("Digite A:"))
b = int(input("Digite B:"))
c = int(input("Digite C:"))

x1 = float
x2 = float

delta = float (b**2 - 4 * a * c)
x1 = (-b + delta** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)

os.system("cls")

print("\n => RESULTADOS <=")

print("Delta:", delta)
print("Resultado X +:", x1)
print("Resultado X -:", x2)

