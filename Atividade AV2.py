#Dias da semana
dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
emprestimos = []

#recbeer os dados de quantidade de livros por dia
for dia in dias_semana:
    quantidade = int(input(f"Digite a quantidade de livros de {dia}:\n "))
    emprestimos.append(quantidade)

#Ver quantos livros sao emprestados
total_Liv = sum(emprestimos)
media_Dia = total_Liv / len(emprestimos)

#Encontrar o valor de empresstimos por dia
Maior_val = max(emprestimos)
indice_maior = emprestimos.index(Maior_val)
Dia_Mai = dias_semana[indice_maior]

# mostrar resultados
print("\nRelatório Semanal de Empréstimos")
print(f"Total de livros emprestados: {total_Liv}")
print(f"Média diária de empréstimos: {media_Dia}")
print(f"O dia com maior movimento foi {Dia_Mai} com {Maior_val} livros.")