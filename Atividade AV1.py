while True:
    try:
        #dias atrasados
        dias_atrasados = int(input(f"Qual foi o tempo de atraso? \n"))
        break
    except ValueError:
        print("insira valores validos")

#converter int para float
dias_atrasados = float(dias_atrasados)
#O calculo para definir o valor a ser pago de multa
if dias_atrasados <= 3:
    valor_multa = dias_atrasados * 0.50
elif 4 <= dias_atrasados <= 7:
    valor_multa = (0.50 *3) + ((dias_atrasados - 3) * 1.00)
else:
    valor_multa = (0.50 *3 + 4*1) + ((dias_atrasados - 7) * 2.00)

# Exibição do resultado usando f-string para formatar duas casas decimais
print(f"O valor da sua multa é R$ {valor_multa}")