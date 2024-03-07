# %% [markdown]
# ## Instalar e carregar as bibliotecas

# %%
# pip install pandas seaborn matplotlib

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %% [markdown]
# ## 2. Carregar dados

# %%
df = pd.read_csv("survey.csv")
df.head()

# %% [markdown]
# ## 3. Limpando os dados
# 
# 1. remover dados faltantes
# 2. remover duplicatas
# 3. remover colunas com baixa utilidade

# %%
df.info()

# %%
# Elimina todas as linhas com dados faltantes
df = df.dropna()

# Mostra informações do DataFrame
df.info()

# %%
# Identifica as linhas duplicadas
duplicadas = df[df.duplicated()]

# Remove as linhas duplicadas
df = df.drop_duplicates()

# Imprime as linhas duplicadas que foram removidas
print(duplicadas)

# %%
# Remove a coluna "User_id"
df = df.drop("User_id", axis=1)

# %%
df.info()

# %% [markdown]
# ## 4. Calculando estatísticas descritivas

# %%
df.describe()
