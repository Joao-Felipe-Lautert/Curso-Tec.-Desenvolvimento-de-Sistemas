#Atividade proposta pelo professor Douglas Scariot na matéria de Programação Back-End

#loop de repetição para funcionamento infinito
while 1 > 0:
   #input do nome e dos números
    nome = str(input("Digite seu nome:\n"))
    primeiro_numero = float(input("Digite o primeiro número:\n"))
    segundo_numero = float(input("Digite o segundo número:\n"))
    
    #realiza as operações
    soma = float(primeiro_numero + segundo_numero)
    subtracao = float(primeiro_numero - segundo_numero)
    multiplicacao = float(primeiro_numero * segundo_numero)
    divisao = float(primeiro_numero / segundo_numero)
    
    #devolve os resultados
    print(f"{nome} o resultado das operações são:")
    print(f"O resultado da soma de {primeiro_numero} + {segundo_numero} é {soma}")
    print(f"O resultado da subtração de {primeiro_numero} - {segundo_numero} é {subtracao}")
    print(f"O resultado da multiplicação de {primeiro_numero} * {segundo_numero} é {multiplicacao}")
    print(f"O resultado da divisão de {primeiro_numero} / {segundo_numero} é {divisao}")