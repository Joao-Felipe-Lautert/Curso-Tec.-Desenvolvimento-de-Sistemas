# Desenvolva um pequeno aplicativo, somente em modo texto que receba uma frase do usuário e conte as vogais e caracteres totais da frase.
# Matéria de Programação Back-End
# Feito por: João Felipe Lautert, Nº:16, 3º D.S

print("--- Super Analisador de Texto ---")
frase = input("Digite sua frase ou texto: ")

# Definições de conjuntos de caracteres
vogais_ref = "aeiouáéíóúâêîôûàèìòùãõ"
consoantes_ref = "bcdfghjklmnpqrstvwxyz"

# Inicialização dos contadores
cont_vogais = 0
cont_consoantes = 0
cont_numeros = 0

# 1. Contagem de Palavras: divide a frase por espaços e conta os itens
# O .split() remove espaços extras automaticamente
palavras = frase.split()
total_palavras = len(palavras)

# 2. Percorre cada caractere para as outras contagens
for char in frase.lower(): # O .lower() transforma em minúsculo para comparar melhor
    if char in vogais_ref:
        # Conta as vogais
        cont_vogais += 1
    elif char in consoantes_ref:
        # Conta as consoantes
        cont_consoantes += 1
    elif char.isdigit():
        # Conta os numeros
        cont_numeros += 1

# Exibe os resultados
print("\n" + "="*30)
print(f"Palavras: {total_palavras}")
print(f"Vogais: {cont_vogais}")
print(f"Consoantes: {cont_consoantes}")
print(f"Números (dígitos): {cont_numeros}")
print(f"Total de caracteres: {len(frase)}")
print("="*30)