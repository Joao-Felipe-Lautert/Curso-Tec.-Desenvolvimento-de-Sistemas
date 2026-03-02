#Atividade proposta pelo professor Douglas Scariot na matéria de Programação Back-End
def geral():
   #loop de repetição para funcionamento infinito
   while True:
      #linha de separação entre ciclos
      print("-" * 148)
      try:
         #input do nome e dos números
         nome = str(input("Digite seu nome:\n"))
         primeiro_numero = float(input("Digite o primeiro número:\n"))
         segundo_numero = float(input("Digite o segundo número:\n"))

         #realiza as operações
         soma = round(float(primeiro_numero + segundo_numero), 2)
         subtracao = round(float(primeiro_numero - segundo_numero), 2)
         multiplicacao = round(float(primeiro_numero * segundo_numero), 2)
         divisao = round(float(primeiro_numero / segundo_numero), 2)

         #devolve os resultados
         print(f"{nome} o resultado das operações são:")
         print(f"O resultado da soma de {primeiro_numero} + {segundo_numero} é {soma}")
         print(f"O resultado da subtração de {primeiro_numero} - {segundo_numero} é {subtracao}")
         print(f"O resultado da multiplicação de {primeiro_numero} * {segundo_numero} é {multiplicacao}")
         print(f"O resultado da divisão de {primeiro_numero} / {segundo_numero} é {divisao}")

      #Retorna para o início do Loop While em caso de valores não numéricos
      except ValueError:
         print("Insira valores validos")

#Chama a função para ser executada
geral()