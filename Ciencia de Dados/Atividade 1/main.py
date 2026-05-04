import pandas as pd         # Para manipulação e análise de dados (DataFrames)
import matplotlib.pyplot as plt # Para criar gráficos estáticos
import seaborn as sns       # Para criar gráficos estatísticos mais atraentes (baseado no matplotlib)
import os                   # Para interagir com o sistema operacional (ex: verificar existência de arquivos)

def analisar_vendas(caminho_csv="vendas_empresa.csv"):

    # Lê o arquivo CSV de vendas, exibe tabelas de resumo e gera gráficos correspondentes.
    if not os.path.exists(caminho_csv):
        print(f"Erro: O arquivo '{caminho_csv}' não foi encontrado.")
        print("Certifique-se de que o arquivo CSV está na mesma pasta que este script.")
        return

    # Configurações de Estilo
    sns.set_theme(style="dark")
    plt.rcParams["figure.figsize"] = (12, 6)

    try:
        # Carregar dados
        df = pd.read_csv(caminho_csv)
        
        # Converter coluna de data
        df["Data"] = pd.to_datetime(df["Data"])
        
        print("\n" + "="*50)
        print(" RELATÓRIO DE VENDAS CONSOLIDADO ")
        print("="*50)

        # 1. ANÁLISE POR VENDEDOR #
        print("\n[1] ANÁLISE POR VENDEDOR")
        vendedor_resumo = df.groupby("Vendedor")["Valor_Total"].sum().sort_values(ascending=False).reset_index()
        vendedor_resumo.columns = ["Vendedor", "Total Vendido (R$)"]
        print(vendedor_resumo.to_markdown(index=False, numalign="left", stralign="left"))
        
        plt.figure()
        sns.barplot(data=vendedor_resumo, x="Vendedor", y="Total Vendido (R$)", palette="viridis")
        plt.title("Total de Vendas por Vendedor", fontsize=14)
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig("01_vendas_por_vendedor.png")
        print("-> Gráfico '01_vendas_por_vendedor.png' gerado.")

        # 2. ANÁLISE POR MÊS #
        print("\n[2] ANÁLISE POR MÊS")
        df["Mes"] = df["Data"].dt.to_period("M").astype(str)
        mes_resumo = df.groupby("Mes")["Valor_Total"].sum().reset_index()
        mes_resumo.columns = ["Mês", "Total Vendido (R$)"]
        print(mes_resumo.to_markdown(index=False, numalign="left", stralign="left"))
        
        plt.figure()
        sns.lineplot(data=mes_resumo, x="Mês", y="Total Vendido (R$)", marker="o", linewidth=2.5, color="royalblue")
        plt.title("Evolução Mensal de Vendas", fontsize=14)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("02_vendas_por_mes.png")
        print("-> Gráfico '02_vendas_por_mes.png' gerado.")

        # 3. ANÁLISE POR SEMANA #
        print("\n[3] ANÁLISE POR SEMANA")
        # Agrupar por semana (W) e formatar a data para a tabela
        semana_resumo = df.resample("W", on="Data")["Valor_Total"].sum().reset_index()
        semana_resumo["Semana (Início)"] = semana_resumo["Data"].dt.strftime("%Y-%m-%d")
        
        # Tabela (mostrando apenas as colunas relevantes)
        print(semana_resumo[["Semana (Início)", "Valor_Total"]].to_markdown(index=False, numalign="left", stralign="left"))
        
        plt.figure()
        sns.lineplot(data=semana_resumo, x="Semana (Início)", y="Valor_Total", marker="s", color="seagreen")
        plt.title("Desempenho de Vendas por Semana", fontsize=14)
        plt.xticks(rotation=90, ha="center")
        plt.tight_layout()
        plt.savefig("03_vendas_por_semana.png")
        print("-> Gráfico '03_vendas_por_semana.png' gerado.")

        print("\n" + "="*50)
        print(" PROCESSO CONCLUÍDO COM SUCESSO! ")
        print("="*50)

    except Exception as e:
        print(f"Ocorreu um erro durante o processamento: {e}")

#Chama a função quando o script é executado diretamente
if __name__ == "__main__":
    analisar_vendas("vendas_empresa.csv")
