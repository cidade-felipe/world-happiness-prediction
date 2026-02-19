# 🌍 World Happiness Prediction

Este projeto analisa os dados do **World Happiness Report (2005–2022)** com dois grandes focos:

1. **Modelagem preditiva em Python**
2. **Dashboard analítico interativo no Power BI**

O objetivo é entender quais fatores socioeconômicos explicam melhor o **Índice de Felicidade** global e como esses fatores se relacionam ao longo do tempo.

Dataset original:
[https://www.kaggle.com/datasets/usamabuttar/world-happiness-report-2005-present](https://www.kaggle.com/datasets/usamabuttar/world-happiness-report-2005-present)

---

# 🎯 Objetivos

* Construir pipeline completo de ETL e tratamento de dados
* Comparar modelos de regressão para prever felicidade
* Interpretar resultados com SHAP
* Desenvolver dashboard interativo com regressões dinâmicas
* Permitir análise por ano único ou todos os anos combinados
* Explorar correlações entre felicidade e variáveis socioeconômicas

---

# 🧠 Modelagem Preditiva

Modelos avaliados:

| Modelo           | R²        | RMSE      | Observação                              |
| ---------------- | --------- | --------- | --------------------------------------- |
| Regressão Linear | 0.755     | 0.535     | Captura tendência geral                 |
| **Random Forest**    | **0.856** | **0.410** | **Melhor desempenho**                       |
| XGBoost          | 0.850     | 0.418     | Alto desempenho com potencial de tuning |

Principais variáveis associadas à felicidade segundo SHAP:

* PIB per capita
* Afeto positivo
* Apoio social
* Expectativa de vida
* Liberdade de escolhas
* Percepções de corrupção

---

# 📊 Dashboard Power BI

O relatório interativo foi estruturado em três páginas principais (conforme o relatório exportado ):

## 1️⃣ Visão Geral

Contém:

* Índice médio de felicidade por ano
* Top 5 países mais felizes
* Top 5 países menos felizes
* Indicadores médios globais:

  * PIB per capita médio
  * Apoio social médio
  * Expectativa de vida média
  * Liberdade de escolhas
  * Confiança no governo nacional
* Segmentador de ano (Ano único ou Todos)

Permite análise temporal e comparação global.

---

## 2️⃣ Correlações e Regressões

Página central do projeto analítico.

Contém scatter plots com linha de regressão linear dinâmica para:

* PIB per capita
* Apoio Social
* Expectativa de vida
* Generosidade
* Liberdade de escolhas
* Percepções de corrupção
* Confiança no governo nacional

Funcionalidades implementadas:

* Regressão calculada com `LINESTX` em DAX
* Inclinação (Slope) e Intercept dinâmicos
* Funcionamento com:

  * Um único ano selecionado
  * Múltiplos anos
  * Todos os anos
* Alternância de variáveis via botões (Bookmarks)
* Sobreposição de reta usando tabela de eixo auxiliar

Essa parte mostra domínio de modelagem analítica avançada dentro do Power BI.

---

## 3️⃣ Mapa Global

Mapa mundial com coloração por índice médio de felicidade.

Inclui:

* Escala dinâmica
* Filtro por ano
* Distribuição geográfica do bem-estar

Observação: o visual de mapa padrão apresenta aviso de futura descontinuação (conforme página 3 do relatório ).

---

# 📂 Estrutura do Projeto

```
world-happiness-prediction/
│
├── chars/
│   └── data/
│       └── dataset_comparacao_modelos.csv
│
├── data/
│   └── processed/
│       ├── world_happiness_preprocessed.csv
│       └── World Happiness Report.csv
│
├── modules/
│   ├── translate_column_pais.py
│   └── traslate_columns_dataset.py
│
├── notebooks/
│   ├── global_insights.ipynb
│   ├── preprocessed.ipynb
│   └── train.ipynb
│
├── reports/
│   ├── world_hapiness_report.csv
│   └── world-happiness-prediction-report.pbix
│
├── venv/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

# 🔬 Técnicas Utilizadas

## Python

* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* SHAP
* Matplotlib
* Seaborn
* GeoPandas
* Plotly

## Power BI

* DAX avançado
* LINESTX
* ADDCOLUMNS + SUMMARIZE
* Bookmarks
* Seleção dinâmica de variáveis
* Regressão linear manual
* Tabelas de eixo auxiliares
* Interações entre visuais

---

# 💡 Diferenciais Técnicos

* Regressão implementada manualmente em DAX
* Alternância dinâmica entre múltiplas variáveis independentes
* Análise temporal controlada por segmentador
* Integração entre Machine Learning em Python e BI interativo
* Estrutura modular de notebooks
* Projeto pronto para portfólio técnico

---

# 🚀 Próximos Passos Possíveis

* Implementar regressão múltipla no Power BI
* Calcular e exibir R² dinamicamente no dashboard
* Substituir mapa padrão por visual mais moderno
* Adicionar análise por clusters de países

---

# 📄 Licença

Licença MIT
Copyright © 2026 Felipe Cidade