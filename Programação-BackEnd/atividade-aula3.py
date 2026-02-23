#Crie um programa que receba 2 números, some-os, e retorne o resultado ao Usúario
def perguntas():
    numero1 = float(input("Digite o 1º Número: \n"))

    numero2 = float(input("Digite o 2º Número: \n"))

    print("Operações Possíveis: + - * /")
    operacao = str(input("Digite a operação desejada: \n"))
    return numero1, numero2, operacao
numero1, numero2, operacao = perguntas()

if operacao == "+":
    resultadoSoma = float(numero1 + numero2)
    print(f"O resuldado da soma é: {resultadoSoma}")
elif operacao == "-":
    resultadoSub = float(numero1 - numero2)
    print(f"O resuldado da soma é: {resultadoSub}")
elif operacao =="*":
    resultadoMult = float(numero1 * numero2)
    print(f"O resuldado da soma é: {resultadoMult}")
elif operacao == "/":
    resultadoDiv = float(numero1 / numero2)
    print(f"O resuldado da soma é: {resultadoDiv}")
else:
    print("Operação Indefinida. Voltando ao início")
    perguntas()
