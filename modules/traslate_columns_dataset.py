import pandas as pd
from googletrans import Translator
import os

# Garantir caminho correto do CSV independente do local de execução
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "../data/world_happiness_report.csv")

df = pd.read_csv(file_path)

translator = Translator()
colunas_traduzidas = {}

for col in df.columns:
   try:
      traducao = translator.translate(col, src='en', dest='pt').text
      colunas_traduzidas[col] = traducao
   except Exception:
      colunas_traduzidas[col] = col

df = df.rename(columns=colunas_traduzidas)

print("Colunas traduzidas:")
print(df.columns.tolist())

# Salvar o CSV traduzido
df.to_csv(os.path.join(base_path, "../data/world_happiness_report_pt.csv"), index=False)
