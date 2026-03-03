import random

nickname = str(input("digite o nome do seu personagem\n"))

print ("Este é um jogo de adivinhação de números, onde o jogador tem que tentar descobrir um número secreto gerado aleatoriamente. O número varia conforme o nível de dificuldade que o jogador escolhe.\nO objetivo do jogo é acertar o número secreto antes de esgotar o número máximo de tentativas, que também depende do nível de dificuldade. Vamos detalhar os principais pontos do jogo:")
print ("1-Dificuldade Fácil 1 - Fácil (Número entre 1 e 50 | 10 tentativas)\n2-Dificuldade Média (Número entre 1 e 100 | 8 tentativas)\n3-Dificuldade Dificil (Número entre 1 e 500 | 12 tentativas)")

dificuldade = str(input("Celecione sua dificuldade:\n"))

    if dificuldade == "F" or "f" or "fácil" or "Fácil" or "facil" or "Facil" or "1":
        limite = 50
        tentavias = 10
        print ("Dificculdade escolhida: Fácil")
    elif dificuldade == "M" or "m" or "media" or "Media" or "média" or "Média" or "2":
        limite = 100
        tentavias = 8
        print ("Dificculdade escolhida: Média")
    elif dificuldade == "D" or "d" or "dificil" or "Dificil" or "difícil" or "Difícil" or "3":
        limite = 500
        tentavias = 12
        print ("Dificculdade escolhida: Difícil")
    else:
            print("Dificuldade não definida! Tente novamente.\n")

print(f"{nickname} o numero aleatorio foi escolhido boa sorte")
