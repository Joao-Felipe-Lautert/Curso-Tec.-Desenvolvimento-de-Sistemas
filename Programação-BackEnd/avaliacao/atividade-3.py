# Definição de váriaveis
porcentagemPaginas = float()
valorX = float()
valorParcial = float()
valorFinal = float()
paginaslidasAcumulado = float()
totalPaginas = float(input("Digite o número total de páginas do livro: \n"))

while True:
    try:
        paginasLidas = float(input("Digite o número de páginas lidas do livro: \n"))
        # Se as páginas lidas forem maior que o total de páginas, retorna um erro
        if paginasLidas > totalPaginas:
            # Personaliza a mensagem no ValueError
            raise ValueError("O número de páginas lidas não podem ser maiores que o número de páginas do livro, digite um número válido: \n")
        # Lógica de calculo
        # Pimeiro multiplica o número de paginas lidas por 100
        # Depois divide o valor desse calculo pelo total de paginas
        # Possuindo a função round para arredondar em no máximo 2 casas decimais
        valorX = paginasLidas * 100
        valorParcial = round((valorX / totalPaginas), 2)
        # Lógica de aculumação
        # Somando para variaveis de controle a cada vez que o código é "reiniciado"
        paginaslidasAcumulado += paginasLidas
        valorFinal += valorParcial
        # Retorno ao usuário
        print(f"A porcentagem de leitura do livro é {valorFinal}%")
        if paginaslidasAcumulado == totalPaginas:
            print("Você já leu todo livro.")
            break
    # retorna o erro com a mensagem personalizada
    except ValueError as e:
        print(f"Erro de entrada: {e}")
