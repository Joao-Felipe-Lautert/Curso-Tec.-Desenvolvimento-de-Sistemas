while True:
    try:
        # Input de dados
        diasAtrasoINT = int(input("Quantos dias a devolução está atrasada? \n"))
        break
    except ValueError:
        print("Insirá dados validos!")

# Definição de variáveis
multa = 0
multaTemp = 0

# conversão de int para float
diasAtraso = float(diasAtrasoINT)

# Custos de atraso por período
ateTres = float(0.50)
deQuatroaSete = float(1.00)
maisdeSete = float(2.00)

if diasAtraso <= 3:
    multa = float(diasAtraso * ateTres)

elif diasAtraso >= 4 or diasAtraso <= 7:
    multa = float((ateTres * 3) + (diasAtraso - 3) * 1.00)
elif diasAtraso > 7:
    multa = float((ateTres * 3) + (diasAtraso - 7) * 2.00)

#Exibição
print(f"O valor da sua Multa é R${multa}")