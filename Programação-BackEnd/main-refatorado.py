#Código de verificação de cidadania
#Autoria colaborativa de:
#João Felipe Lautert
#Felipe Prestes Belusso7
#Desafio proposto pelo Professor Douglas Scarot, na matéria de Programação Back-End
def obter_dados():
    while True:
        try:
            valor = float(input("Digite sua Idade: "))
            tipo = input("Digite (D) para dias, (M) para meses ou (A) para anos: ").upper()
            eleitor = int(input("Digite 1 se tiver título de Eleitor e 2 se não tiver: "))
            
            # Cálculo da idade em anos baseado no tipo
            if tipo == 'A':
                idade_anos = valor
            elif tipo == 'M':
                idade_anos = valor / 12
            elif tipo == 'D':
                idade_anos = valor / 365.25
            else:
                print("Tipo inválido! Tente novamente.")
                continue

            # Validação de idade biológica
            if idade_anos > 150 or idade_anos < 0:
                print(f"Idade de {round(idade_anos, 1)} anos parece incorreta. Tente novamente.")
                continue
            
            return idade_anos, eleitor
        except ValueError:
            print("Por favor, digite valores numéricos válidos.")

# Fluxo Principal
idade, tem_titulo = obter_dados()
idade_formatada = round(idade, 1)

print("-" * 30)
# Lógica de Cidadania
if idade >= 16 and tem_titulo == 1:
    print(f"Parabéns! Com {idade_formatada} anos, você é um cidadão.")
elif idade >= 16:
    print(f"Com {idade_formatada} anos, você não é cidadão, mas pode tirar seu título.")
else:
    print(f"Com {idade_formatada} anos, você ainda não pode ser considerado cidadão eleitor.")

# Lógica de Voto
if tem_titulo == 1:
    if 18 <= idade < 70:
        print("Seu voto é OBRIGATÓRIO.")
    elif 16 <= idade < 18 or idade >= 70:
        print("Seu voto é OPCIONAL.")
else:
    if idade < 16:
        print("Você ainda não tem idade para votar.")
    else:
        print("Você tem idade, mas precisa do título para votar.")
