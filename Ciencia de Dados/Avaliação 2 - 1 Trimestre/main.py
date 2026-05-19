import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar o arquivo CSV (0,5 ponto)
df = pd.read_csv('alugueis.csv')

# 2. Verificar valores ausentes (1,0 ponto)
print("--- Quantidade de valores ausentes por coluna ---")
print(df.isnull().sum())
print("-" * 50)

# 3. Tratar valores ausentes (2,0 pontos)
# Preencher preco_aluguel com a mediana
mediana_preco = df['preco_aluguel'].median()
df['preco_aluguel'] = df['preco_aluguel'].fillna(mediana_preco)

# Preencher quartos com a moda (usamos [0] pois .mode() retorna uma Série)
moda_quartos = df['quartos'].mode()[0]
df['quartos'] = df['quartos'].fillna(moda_quartos)

# 4. Remover outlier (2,0 pontos)
# Remove imóveis com area_m2 > 300 E preco_aluguel < 500 simultaneamente
condicao_outlier = (df['area_m2'] > 300) & (df['preco_aluguel'] < 500)
df = df[~condicao_outlier]

# 5. Criar nova coluna (1,0 ponto)
df['custo_por_m2'] = df['preco_aluguel'] / df['area_m2']

# 6. Exibir estatísticas por bairro (1,5 ponto)
print("\n--- Estatísticas descritivas do custo por m² por bairro ---")
print(df.groupby('bairro')['custo_por_m2'].describe())
print("-" * 50)

# 7. Gerar histograma (1,5 ponto)
plt.hist(df['custo_por_m2'], bins=10, edgecolor='black')
plt.title("Distribuição do Custo por m²")
plt.xlabel("Custo por m² (R$)")
plt.ylabel("Frequência")
plt.show()

# 8. Mensagem final (0,5 ponto)
bairro_maior_custo = df.groupby('bairro')['custo_por_m2'].mean().idxmax()
print(f"\nBairro com maior custo médio por m²: {bairro_maior_custo}")