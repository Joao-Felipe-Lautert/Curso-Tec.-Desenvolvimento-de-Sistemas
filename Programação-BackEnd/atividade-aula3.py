#Crie um programa que receba 2 números, some-os, e retorne o resultado ao Usúario
#Desáfio proposto pelo Professor Douglas Scariot, na matéria de Programação Back-End

#Função que garante a execução continua do código (Código executa eternamente)
def perguntas():
    while True:
        #Printa "-" 30 vezes para divisão de cada loop do código rodado
        print("-" *30)
        try:
            #Inserção de dados por meio de perguntas ao usuário
            numero1 = float(input("Digite o 1º Número: \n"))
            numero2 = float(input("Digite o 2º Número: \n"))
            print("Operações Possíveis: + | - | * | /")
            operacao = str(input("Digite a operação desejada: \n"))
            #Cadeia de Cálculo
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
                #Retorna para o início do Loop While em caso de Operação Indefinida
                continue
        #Retorna para o início do Loop While em caso de valores não numéricos
        except ValueError:
            print("Insira valores validos")

#Chama a função para ser executada
perguntas()

#Para parar o programa, exclua o terminal no qual ele está rodando
