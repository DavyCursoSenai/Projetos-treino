import os
os.system("cls")



while True:
    print("CALCULADORA")
    print("+ -> SOMA")
    print("- -> SUBTRAÇÃO")
    print("x -> MULTIPLICAÇÃO")
    print("/ -> DIVISÃO")
    

    primeiro_numero = float(input("Digite o primeiro número:"))

    operacao = input("Escolha a operação:")

    segundo_numero = float(input("Digite o segundo número:"))

    soma = primeiro_numero + segundo_numero
    subtracao = primeiro_numero - segundo_numero
    multiplicacao = primeiro_numero * segundo_numero
    divisao = primeiro_numero / segundo_numero




    if operacao == '+':
        print(f"A soma de {primeiro_numero} com {segundo_numero} é = ", soma )
        
    elif operacao == '-':
        print(f"A subtração de {primeiro_numero} com {segundo_numero} é =", subtracao)

    elif operacao == 'x':
        print(f"A multiplicação de {primeiro_numero} com {segundo_numero} é =", multiplicacao)

    elif operacao == '/':
        print(f"A divisão de {primeiro_numero} com {segundo_numero} é = ", divisao)

    

        


