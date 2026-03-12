# Lista com os nomes dos dias
dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
arrayemprestimos = []

# Input de dados usando a lista de nomes
for dia in dias_semana:
    while True:
        try:
            # Agora usamos a variável 'dia' diretamente na string
            emprestimoDias = int(input(f"Digite o numero de livros emprestado {dia}: \n"))
            arrayemprestimos.append(emprestimoDias)
            break
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

# Cálculos (Soma e Média)
totalLivrosSemana = sum(arrayemprestimos)
mediaLivrosSemana = totalLivrosSemana / len(arrayemprestimos)

# Para encontrar o dia com maior valor de forma legível:
maiorValor = max(arrayemprestimos)
diaMaiorValor = dias_semana[arrayemprestimos.index(maiorValor)]

# Exibição para o Usúario
print(f"O total de livros emprestados na semana foi de {totalLivrosSemana}")
print(f"A média do número de livros emprestados foi de {mediaLivrosSemana}")
print(f"O dia com o maior número de livros emprestados é {diaMaiorValor} com um total de {maiorValor} ")