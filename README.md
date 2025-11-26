# World Happiness Prediction

Este projeto utiliza dados do **World Happiness Report** para analisar fatores socioeconômicos e prever o **Índice de Felicidade** de países ao longo dos anos. A abordagem envolve pré-processamento, modelagem preditiva e interpretações com técnicas modernas de explicabilidade.

O dataset original pode ser acessado em:
[https://www.kaggle.com/datasets/jahaidulislam/world-happiness-report-2005-2021](https://www.kaggle.com/datasets/jahaidulislam/world-happiness-report-2005-2021)

---

## 📌 Objetivos do Projeto

* Construir um pipeline de pré-processamento com foco em integridade e consistência.
* Comparar algoritmos de regressão (Linear, Random Forest e XGBoost) para prever felicidade.
* Interpretar os modelos com **SHAP values**, identificando fatores determinantes.
* Realizar visualizações interativas e mapas temáticos globais.

---

## 📊 Modelagem e Resultados

| Modelo            | R² (Explicação) | RMSE (Erro Médio) | Observação                                                     |
| ----------------- | --------------- | ----------------- | -------------------------------------------------------------- |
| Regressão Linear  | 0.755           | 0.535             | Representa bem a tendência geral, perde precisão nos extremos. |
| **Random Forest** | **0.856**       | **0.410**         | Melhor desempenho geral sem ajuste profundo.                   |
| XGBoost           | 0.850           | 0.418             | Competitivo, tende a melhorar com tuning avançado.             |

A análise interpretativa (SHAP) mostrou que os fatores mais associados ao bem-estar global incluem: **PIB per capita, afeto positivo, apoio social, expectativa de vida e liberdade de escolhas**, enquanto **percepção de corrupção e emoções negativas** reduzem significativamente a felicidade.

---

## 🌍 Visualização Global da Felicidade

Além dos gráficos comparativos por país, foi desenvolvido um **mapa mundial interativo** que colore cada país de acordo com o índice de felicidade em um determinado ano.

### 📦 Dependências para o mapa geográfico

```bash
pip install geopandas geodatasets pyproj shapely rtree descartes
```

### 🔁 Padronização de nomes dos países

Como os nomes dos países no Kaggle não coincidem exatamente com os nomes da base cartográfica (Natural Earth), foi necessário padronizar as nomenclaturas antes de gerar o mapa. O seguinte dicionário foi utilizado:

```python
correcao_paises = {
    "United States": "United States of America",
    "Congo (Kinshasa)": "Democratic Republic of the Congo",
    "Congo (Brazzaville)": "Republic of the Congo",
    "Eswatini": "eSwatini",
    "Hong Kong S.A.R. of China": "Hong Kong",
    "State of Palestine": "Palestine",
    "Taiwan Province of China": "Taiwan",
    "Turkiye": "Turkey",
    "Somaliland region": None  # Região sem reconhecimento cartográfico
}
```

Aplicação:

```python
df["País"] = df["País"].replace(correcao_paises)
```

---

## 📂 Estrutura do Projeto

```
world-happiness-prediction/
│
├── chars/
│   └── data/
│       └── dataset_comparacao_modelos.csv        # Conjunto auxiliar para visualizações
│
├── data/
│   ├── processed/                                # Dados tratados e traduzidos
│   │   ├── world_happiness_report_colunas_pt_preprocessed.csv
│   │   ├── world_happiness_report_colunas_pt.csv
│   │   └── world_happiness_report.csv
│
├── modules/                                      # Scripts utilitários
│   ├── translate_column_pais.py                  # Correções de nomes de países
│   └── traslate_columns_dataset.py               # Tradução e renomeação de colunas
│
├── notebooks/                                    # Notebooks de análise e modelagem
│   ├── global_insights.ipynb                     # Visualizações, mapas e comparações interativas
│   ├── preprocessed.ipynb                        # ETL e limpeza de dados
│   └── train.ipynb                               # Treinamento e avaliação dos modelos
│
├── old/                                          # Versões antigas (não utilizadas)
│
├── venv/                                         # Ambiente virtual (ignorado no Git)
│
├── LICENSE                                       # Licença MIT
├── README.md                                     # Documentação do projeto
└── requirements.txt                              # Dependências do projeto



```

---

## 🧠 Tecnologias Utilizadas

* Python (Pandas, NumPy)
* Machine Learning: Scikit-Learn, XGBoost
* Interpretação: SHAP
* Visualização: Matplotlib, Seaborn, GeoPandas

---

## 📄 Licença

Este projeto é distribuído sob a licença **MIT**.
Copyright © 2025 **Felipe Cidade**