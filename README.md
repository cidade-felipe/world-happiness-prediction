Claro, aqui vai o README atualizado incluindo a referência direta ao dataset do Kaggle, mantendo o mesmo tom profissional:

---

# World Happiness Prediction

Este projeto utiliza dados do **World Happiness Report** para analisar fatores socioeconômicos e prever o **Índice de Felicidade** de países ao longo dos anos. A abordagem combina análise exploratória, pré-processamento de dados e modelagem com diferentes algoritmos de regressão em Machine Learning.

O dataset original foi obtido a partir do Kaggle e pode ser acessado em:
[[https://www.kaggle.com/datasets/usamabuttar/world-happiness-report-2005-present?utm_source=chatgpt.com&select=World+Happiness+Report.csv](https://www.kaggle.com/datasets/usamabuttar/world-happiness-report-2005-present?utm_source=chatgpt.com&select=World+Happiness+Report.csv](https://www.kaggle.com/datasets/jahaidulislam/world-happiness-report-2005-2021))

O objetivo é demonstrar como indicadores econômicos, sociais e emocionais podem ser usados para construir modelos capazes de prever o bem-estar médio de uma população, e identificar quais fatores exercem maior influência nesse resultado.

---

## 📌 Objetivos do Projeto

* Construir um pipeline de pré-processamento com foco em qualidade dos dados.
* Comparar modelos de regressão (Linear, Random Forest e XGBoost) na previsão do Índice de Felicidade.
* Utilizar técnicas de interpretabilidade (SHAP) para identificar variáveis determinantes.
* Organizar o projeto de forma profissional e extensível, com scripts modulares e notebooks independentes.

---

## 📂 Estrutura do Projeto

```
world-happiness-prediction/
│
├── data/
│   ├── processed/
│   │   ├── world_happiness_report_colunas_pt_preprocessed.csv
│   │   ├── world_happiness_report_colunas_pt.csv
│   │   └── world_happiness_report.csv
│
├── modules/
│   ├── translate_column_pais.py
│   └── translate_columns_dataset.py
│
├── notebooks/
│   ├── preprocessed.ipynb
│   └── train.ipynb
│
├── app.py
└── .gitignore
```

---

## 🔎 Modelagem e Resultados

Foram avaliados três modelos:

| Modelo            | R² (Explicação) | RMSE (Erro Médio) | Observação                                                         |
| ----------------- | --------------- | ----------------- | ------------------------------------------------------------------ |
| Regressão Linear  | 0.755           | 0.535             | Representa bem a tendência geral, mas perde precisão nos extremos. |
| **Random Forest** | **0.856**       | **0.410**         | Melhor desempenho geral sem necessidade de tuning complexo.        |
| XGBoost           | 0.850           | 0.418             | Desempenho próximo ao Random Forest, pode melhorar com otimização. |

A análise interpretativa utilizando **SHAP** destacou as variáveis com maior impacto na felicidade global:

* PIB per capita
* Afeto positivo
* Apoio social
* Expectativa de vida
* Liberdade de escolhas
* Percepção de corrupção (impacto negativo)
* Afeto negativo (impacto negativo)

Esses resultados reforçam que o bem-estar coletivo depende de uma combinação entre condições materiais, vínculos sociais, estabilidade emocional e confiança nas instituições.

---

## 🧠 Tecnologias Utilizadas

* Python 3
* Pandas, NumPy
* Scikit-Learn
* XGBoost
* SHAP
* Matplotlib / Seaborn

---

## 🚀 Possíveis Extensões Futuras

* Aplicação web com Streamlit para previsões interativas.
* Otimização automática (GridSearch/RandomizedSearch) de hiperparâmetros.
* Inclusão de indicadores culturais e demográficos.
* Visualizações geográficas interativas.

---

## 📄 Licença

Este projeto é distribuído sob a licença **MIT**.
Copyright © 2025 **Felipe Cidade**

---

Se quiser, ainda posso gerar um:

📌 `requirements.txt`
📌 `.gitignore` otimizado para notebooks + Python
📌 badge visual pro README (ex: MIT, Python version)

Quer algum deles?
