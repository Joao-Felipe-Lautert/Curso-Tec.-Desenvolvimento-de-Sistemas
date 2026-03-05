import random


nickname = str(input("digite o nome do seu personagem\n"))

print ("Este é um jogo de adivinhação de números, onde o jogador tem que tentar descobrir um número secreto gerado aleatoriamente. O número varia conforme o nível de dificuldade que o jogador escolhe.\nO objetivo do jogo é acertar o número secreto antes de esgotar o número máximo de tentativas, que também depende do nível de dificuldade. Vamos detalhar os principais pontos do jogo:")
print ("1-Dificuldade Fácil (Número entre 1 e 50 | 10 tentativas)\n2-Dificuldade Média (Número entre 1 e 100 | 8 tentativas)\n3-Dificuldade Dificil (Número entre 1 e 500 | 12 tentativas)")

inputDificuldade = str(input("Celecione sua dificuldade:\n"))

if inputDificuldade == "F" or "f" or "fácil" or "Fácil" or "facil" or "Facil" or "1":
    numeroLimite = 50
    mumeroAleatorio = random.randint(0, 50)
    limiteTentavias = 10
    dificuldade = 1
    print ("Dificculdade escolhida: Fácil")
elif inputDificuldade == "M" or "m" or "media" or "Media" or "média" or "Média" or "2":
    numeroLimite = 100
    mumeroAleatorio = random.randint(0, 100)
    limiteTentavias = 8
    dificuldade = 2
    print ("Dificculdade escolhida: Média")
elif inputDificuldade == "D" or "d" or "dificil" or "Dificil" or "difícil" or "Difícil" or "3":
    numeroLimite = 500
    mumeroAleatorio = random.randint(0, 500)
    limiteTentavias = 12
    dificuldade = 3
    print ("Dificculdade escolhida: Difícil")
else:
    print("Dificuldade não definida! Tente novamente.\n")

print(f"{nickname} o numero aleatorio foi escolhido boa sorte")

def pedir_numero(limiteTentativas, numeroLimite, numeroAleatorio):
    try:
        for tentativas <= limiteTentativas:
            # Tentamos converter a entrada para um número inteiro
            numeroTentativa = int(input("Digite um número inteiro: "))
            print(f"Você digitou o número {numeroTentativa}.")
        if numeroTentativa <= numeroLimite:
            if 
        else:
            print(f"Insira um número válido, dentro do limite de {numeroLimite}")

    except ValueError:
        # Se o usuário digitar letras, o Python gera um ValueError
        print("Erro: Você só pode digitar números inteiros. Tente novamente.")

pedir_numero()
