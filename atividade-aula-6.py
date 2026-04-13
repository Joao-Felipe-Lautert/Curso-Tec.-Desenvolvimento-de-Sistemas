# ira pedir a frase
frase = input("Digite uma frase:\n")

# ira ver o que é vogal ou não é vogal
vogais_referencia = "aeiouAEIOUáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãõÃÕàèìòùÀÈÌÒÙ"

# conta as vogais
contador_vogais = 0

# lê cada caracter da frase
for caractere in frase:
    if caractere in vogais_referencia:
        contador_vogais += 1

# Calcula todos os caracteres ate mesmo espaços e a pontuação
total_caracteres = len(frase)

# Resultado
print("-" * 30)
print(f"Resultados para: '{frase}'")
print(f"Total de caracteres: {total_caracteres}")
print(f"Total de vogais: {contador_vogais}")
print("-" * 30)
