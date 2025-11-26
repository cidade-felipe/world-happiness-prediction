from googletrans import Translator
import pandas as pd
import os

# Garantir caminho correto
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "../data/world_happiness_report_pt.csv")

df = pd.read_csv(file_path)

translator = Translator()

# Identificar automaticamente a coluna que representa o país
coluna_pais = None
for nome in df.columns:
   if "país" in nome.lower() or "country" in nome.lower():
      coluna_pais = nome
      break

if coluna_pais is None:
   raise Exception("Nenhuma coluna referente ao país foi encontrada.")

# Traduzir os valores da coluna de país
valores_traduzidos = []
for valor in df[coluna_pais]:
   try:
      traducao = translator.translate(valor, src='en', dest='pt').text
      valores_traduzidos.append(traducao)
   except:
      valores_traduzidos.append(valor)

df[coluna_pais] = valores_traduzidos

# Salvar novamente o dataset
df.to_csv(os.path.join(base_path, "../data/world_happiness_report_pt.csv"), index=False)

print(f"A coluna '{coluna_pais}' foi traduzida com sucesso.")
