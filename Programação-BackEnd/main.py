#Definição das variaveis de variações de input's de idade
inpuIdadeDias = float(0)
inputIdadeMeses = float(0)
inputIdadeAnos = float(0)

#Função que armazena as perguntas
def perguntas():
    #Variavel do tipo Inteiro Receba Idade Digitada
    inputIdade = float(input ("Digite sua Idade \n")) 
    #Varíavel do tipo String, que recebe se a idade foi digitada em anos ou em dias
    tipoIdade = str(input("Se idade em dias digite D, se em Anos digite A e se em meses M: \n"))
    #Variavel eleitor (Inteira é recebida do usuario)
    eleitor = int(input("Digite 1 se tiver titulo de Eleitor e 2 se nao tiver \n"))
    return inputIdade, tipoIdade, eleitor
inputIdade, tipoIdade, eleitor = perguntas()

# Filtra os dados de Idade em Meses, Dias e Anos
if inputIdade > 150:
    inputIdadeMeses = inputIdade
elif inputIdade > 150:
    inpuIdadeDias = inputIdade
elif inputIdade <= 150:
    inputIdadeAnos = inputIdade

#Verifica se a idade foi digitada em dias ou anos e partir disso, calculá quantos anos a pessoa tem
if inputIdadeAnos > 150:
    print("Falso Idoso, para de mentir, coloque os dados corretamente.")
    perguntas()
elif "M" in tipoIdade:
    idadeAnos = inputIdade / 12
elif "D" in tipoIdade:
    idadeAnos = inputIdade / 365.25
elif "A" in tipoIdade:
    idadeAnos = inputIdade
else:
    print("Tipo de Idade Não especificado! Reinsira os dados: \n")
    perguntas()

#Arredonda a idade para o mais próximo
idadeAnos1Casa = round(idadeAnos, 1)

#Se a idade for maior ou igual a 16 e a pessoa tiver titulo de eleitor imprime q a pessoa é cidadao
if idadeAnos >= 16 and eleitor == 1:
    print(f"Parabéns, você é um cidadão e tem aproximadamente {idadeAnos1Casa} anos de idade.")
#Se idade for maior ou igual a 16 e nao tiver titulo de eleitor imprime o que tem entre aspas
elif idadeAnos >= 16 and eleitor == 2:
    print (f"Você não é cidadão, mas tem aproximadamente {idadeAnos1Casa} de idade e pode ser.")
#Se a pessoa for menor de 16 anos, imprime que não pode ser consideradá cidadã
elif idadeAnos < 16 and eleitor == 2 and 1:
    print (f"Você não é cidadão, tem aproximadamente {idadeAnos1Casa} anos de idade, e não pode ser.")
#Se os 2 ifs forem negados imprima voce nao é cidadao
else:
    print(f"Você tem aproximadamente {idadeAnos1Casa} de idade e não é cidadão.")

#Se tiver titulo de eleitor e a idade for maior q 18 e menor q 70 seu voto é obrigatorio, ira imprimir seu voto é obrigatorio
if idadeAnos >= 18 and idadeAnos <70 and eleitor == 1:
    print("Seu voto é obrigatório")
#Se tiver titulo de eleitor e a idade for maior de 70, ira imprimir seu voto é opcional
elif ((idadeAnos < 18 and idadeAnos >=16) or idadeAnos >=70) and eleitor == 1:
    print ("Seu voto é opcional")
#Se a idade da pessoa for menor que 16 anos, imprime que a mesma não pode votar
elif idadeAnos < 16 and (eleitor == 1 or eleitor == 2):
    print("Você não pode votar")
