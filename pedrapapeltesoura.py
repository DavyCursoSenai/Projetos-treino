import random
import os
os.system('cls')

jogo = random.choice(('pedra', 'papel', 'tesoura'))

escolha = input("Digite sua escolha:")



if escolha == 'pedra' and jogo == 'papel':
    print("A máquina escolheu",jogo, 'então', "Você perdeu")
elif escolha == 'papel' and jogo == 'pedra':
    print("A máquina escolheu",jogo, 'então',"Você ganhou")

if escolha == 'tesoura' and jogo == 'pedra':
    print("A máquina escolheu",jogo,'então', "Você perdeu")
elif escolha == 'pedra' and jogo == 'tesoura':
    print("A máquina escolheu",jogo, 'então', "Você ganhou")

if escolha == 'papel' and jogo == 'tesoura':
    print("A máquina escolheu",jogo, 'então', "Você perdeu")
elif escolha == 'tesoura' and jogo == 'papel':
    print("A máquina escolheu",jogo, 'então', "Você ganhou")









