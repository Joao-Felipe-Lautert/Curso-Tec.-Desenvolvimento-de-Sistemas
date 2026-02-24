#Crie um programa que receba 2 números, some-os, e retorne o resultado ao Usúario
#Desáfio proposto pelo Professor Douglas Scariot, na matéria de Programação Back-End

import math

#Função que garante a execução continua do código (Código executa eternamente)
def perguntas():
    while True:
        #Printa "-" 30 vezes para divisão de cada loop do código rodado
        print("-" * 148)
        try:
            #Inserção de dados por meio de perguntas ao usuário
            numero1 = float(input("Digite o 1º Número: \n"))
            numero2 = float(input("Digite o 2º Número: \n"))
            print("Operações Possíveis: + | - | * | / | ^ | raiz | % | !")
            operacao = str(input("Digite a operação desejada: \n"))

            #Cadeia de Cálculo
            if operacao == "+":
                resultado = numero1 + numero2
                print(f"O resuldado da soma é: {resultado}")
            elif operacao == "-":
                resultado = numero1 - numero2
                print(f"O resuldado da subtração é: {resultado}")
            elif operacao =="*":
                resultado = numero1 * numero2
                print(f"O resuldado da multiplicação é: {resultado}")
            elif operacao == "/":
                resultado = numero1 / numero2
                print(f"O resuldado da divisão é: {resultado}")
            elif operacao == "^":
                resultado = numero1 ** numero2
                print(f"O resultado da Potencia é {resultado}")
            elif operacao == "raiz":
                resultado = numero1 ** (1/2)
                resultado1 = numero2 ** (1/2)
                print(f"O resultado da raiz do 1º número é {resultado} e do 2º número é {resultado1}")
            elif operacao == "%":
                resultado = numero1 * (numero2 / 100)
                print(f"O resultado da porcentagem do 2º número sobre o 1º número é {resultado}")
            elif operacao == "!":
                numero1int = int(numero1)
                numero2int = int(numero2)
                resultado = math.factorial(numero1int)
                resultado1 = math.factorial(numero2int)
                print(f"O resultado da fotorial do 1º número é {resultado} e do 2º número {resultado1}")
            else:
                print("Operação Indefinida. Voltando ao início")
                #Retorna para o início do Loop While em caso de Operação Indefinida
                continue
            
        #Retorna para o início do Loop While em caso de valores não numéricos
        except ValueError:
            print("Insira valores validos")

#Chama a função para ser executada
perguntas()
#Para parar o programa, exclua o terminal no qual ele está rodando
