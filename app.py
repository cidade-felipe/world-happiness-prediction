import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# ==========================================================
# CONFIGURAÇÕES INICIAIS
# ==========================================================

st.set_page_config(
   page_title="Liberdade de Escolhas e Qualidade de Vida",
   layout="wide"
)

# Caminho do arquivo (ajuste se necessário)
path = "./data/processed/world_happiness_report_colunas_pt_final.csv"


@st.cache_data
def load_data(csv_path: str) -> pd.DataFrame:
   df_local = pd.read_csv(csv_path)
   return df_local


df = load_data(path)

# ==========================================================
# FUNÇÃO AUXILIAR PARA FORMATAÇÃO EM %
# ==========================================================

def format_percent_cols(df_in: pd.DataFrame, cols) -> pd.DataFrame:
   df_out = df_in.copy()
   for c in cols:
      if c in df_out.columns:
         df_out[c] = (df_out[c] * 100).round(1).astype(str) + "%"
   return df_out

percent_cols = [
   "Liberdade de escolhas",
   "Percepções de corrupção",
   "Confiança no governo nacional",
   "Indice_Bem_Estar",
]

# ==========================================================
# PREPARO DE DADOS
# ==========================================================

all_numeric = [
   "PIB per capita (US$)",
   "Expectativa de vida",
   "Liberdade de escolhas",
   "Percepções de corrupção",
   "Confiança no governo nacional",
]

df_norm = df.copy()
for col in all_numeric:
   col_min = df_norm[col].min()
   col_max = df_norm[col].max()
   if col_max > col_min:
      df_norm[col + "_norm"] = (df_norm[col] - col_min) / (col_max - col_min)
   else:
      df_norm[col + "_norm"] = 0.5

df_norm["Percepções de corrupção_inv_norm"] = 1 - df_norm["Percepções de corrupção_norm"]

df_norm["Indice_Bem_Estar"] = df_norm[
   [
      "Liberdade de escolhas_norm",
      "Expectativa de vida_norm",
      "Confiança no governo nacional_norm",
      "Percepções de corrupção_inv_norm",
   ]
].mean(axis=1)

df = df.merge(
   df_norm[["País", "Ano", "Indice_Bem_Estar"]],
   on=["País", "Ano"],
   how="left"
)

# ==========================================================
# TÍTULO
# ==========================================================

st.title("Liberdade de Escolhas e Qualidade de Vida")

st.write(
   "Este dashboard investiga se a sensação de liberdade para fazer escolhas "
   "está associada a indicadores de qualidade de vida, como expectativa de vida, "
   "percepções de corrupção, confiança no governo e PIB per capita."
)

# ==========================================================
# SIDEBAR - FILTROS GERAIS
# ==========================================================

st.sidebar.header("Filtros")

paises = ["Todos"] + sorted(df["País"].unique())
anos = ["Todos"] + sorted(df["Ano"].unique())

pais_select = st.sidebar.selectbox("Filtrar por país", paises)
ano_select = st.sidebar.selectbox("Filtrar por ano", anos)

df_filtered = df.copy()

if pais_select != "Todos":
   df_filtered = df_filtered[df_filtered["País"] == pais_select]

if ano_select != "Todos":
   df_filtered = df_filtered[df_filtered["Ano"] == ano_select]

# ==========================================================
# 1) MAPA GLOBAL - LIBERDADE DE ESCOLHAS
# ==========================================================

st.subheader("Mapa global da liberdade de escolhas")

if ano_select == "Todos":
   ano_mapa = df["Ano"].max()
   df_map = df[df["Ano"] == ano_mapa]
   st.caption(f"Exibindo o ano mais recente disponível: {ano_mapa}.")
else:
   ano_mapa = ano_select
   df_map = df[df["Ano"] == ano_mapa]

# cópia apenas para hover em %
df_map_show = df_map.copy()
df_map_show["Liberdade de escolhas (%)"] = (df_map_show["Liberdade de escolhas"] * 100).round(1)
df_map_show["Percepções de corrupção (%)"] = (df_map_show["Percepções de corrupção"] * 100).round(1)
df_map_show["Confiança no governo nacional (%)"] = (df_map_show["Confiança no governo nacional"] * 100).round(1)
df_map_show["Indice_Bem_Estar (%)"] = (df_map_show["Indice_Bem_Estar"] * 100).round(1)

fig_map = px.choropleth(
   df_map_show,
   locations="País",
   locationmode="country names",
   color="Liberdade de escolhas",
   hover_name="País",
   hover_data={
      "Liberdade de escolhas (%)": True,
      "Expectativa de vida": True,
      "Percepções de corrupção (%)": True,
      "Confiança no governo nacional (%)": True,
      "PIB per capita (US$)": True,
      "Indice_Bem_Estar (%)": True,
   },
   color_continuous_scale="Blues",
   title=f"Liberdade de escolhas no mundo em {ano_mapa}",
)

st.plotly_chart(fig_map, width="stretch")

# ==========================================================
# 2) SCATTER LIBERDADE x QUALIDADE DE VIDA + REGRESSÃO
# ==========================================================

st.subheader("Liberdade de escolhas x indicadores de qualidade de vida")

metric_scatter = st.selectbox(
   "Escolha a métrica para comparar com Liberdade de escolhas",
   [
      "Expectativa de vida",
      "Percepções de corrupção",
      "Confiança no governo nacional",
      "PIB per capita (US$)",
   ],
)

df_reg = df_filtered.dropna(subset=["Liberdade de escolhas", metric_scatter])

if not df_reg.empty and df_reg["Liberdade de escolhas"].nunique() > 1:
   x = df_reg["Liberdade de escolhas"]
   y = df_reg[metric_scatter]

   slope, intercept = np.polyfit(x, y, 1)
   x_line = np.linspace(x.min(), x.max(), 100)
   y_line = slope * x_line + intercept

   fig_scatter = px.scatter(
      df_reg,
      x="Liberdade de escolhas",
      y=metric_scatter,
      color="Ano",
      hover_name="País",
      size="PIB per capita (US$)",
      title=f"Relação entre Liberdade de escolhas e {metric_scatter}",
   )

   fig_scatter.add_trace(
      go.Scatter(
         x=x_line,
         y=y_line,
         mode="lines",
         name="Regressão linear",
      )
   )

   st.plotly_chart(fig_scatter, width="stretch")
   st.caption(
      f"Tendência aproximada: {metric_scatter} ≈ {slope:.2f} × Liberdade + {intercept:.2f}"
   )
else:
   st.info("Não há dados suficientes, após os filtros, para ajustar uma regressão.")

# ==========================================================
# 3) CORRELAÇÃO ESTATÍSTICA
# ==========================================================

st.subheader("Correlação entre liberdade e qualidade de vida")

df_corr = df_filtered[all_numeric].dropna()

if df_corr.shape[0] > 1:
   corr_matrix = df_corr.corr(method="pearson")

   st.write("Matriz de correlação de Pearson entre as variáveis numéricas:")
   st.dataframe(
      corr_matrix.style.background_gradient(cmap="Blues"),
      use_container_width=True
   )

   if "Liberdade de escolhas" in corr_matrix.columns:
      col_corr = corr_matrix["Liberdade de escolhas"].drop("Liberdade de escolhas")
      st.write("Correlação específica com Liberdade de escolhas:")
      st.dataframe(
         col_corr.to_frame("Correlação").style.bar(),
         use_container_width=True
      )

      st.markdown("Leitura rápida:")
      for var, val in col_corr.items():
         if abs(val) < 0.2:
               nivel = "fraca ou inexistente"
         elif abs(val) < 0.5:
               nivel = "moderada"
         else:
               nivel = "forte"

         sentido = "positiva" if val > 0 else "negativa"
         st.write(
               f"- Relação {nivel} e {sentido} entre Liberdade de escolhas e {var} (r = {val:.2f})."
         )
else:
   st.info("Filtros atuais deixaram poucos dados para cálculo de correlação.")

# ==========================================================
# 4) SÉRIE TEMPORAL POR PAÍS
# ==========================================================

# ==========================================================
# 4) SÉRIE TEMPORAL POR PAÍS (UM INDICADOR POR VEZ)
# ==========================================================

st.subheader("Evolução histórica por país")

if pais_select == "Todos":
   st.info("Selecione um país na barra lateral para ver a evolução histórica.")
else:
   # Escolha do indicador a ser exibido
   metric_time = st.selectbox(
      "Escolha o indicador para a série temporal",
      [
         "Liberdade de escolhas",
         "Expectativa de vida",
         "Confiança no governo nacional",
         "PIB per capita (US$)",
      ],
   )

   df_country = df[df["País"] == pais_select].sort_values("Ano")

   fig_time = px.line(
      df_country,
      x="Ano",
      y=metric_time,
      markers=True,
      title=f"Evolução de {metric_time} em {pais_select}",
   )

   st.plotly_chart(fig_time, width="stretch")


# ==========================================================
# 5) TABELA DINÂMICA + DOWNLOAD
# ==========================================================

st.subheader("Tabela dinâmica por país e ano")

metric_pivot = st.selectbox(
   "Escolha a métrica para a tabela dinâmica",
   [
      "Liberdade de escolhas",
      "Expectativa de vida",
      "Confiança no governo nacional",
      "Percepções de corrupção",
      "PIB per capita (US$)",
      "Indice_Bem_Estar",
   ],
)

pivot = df.pivot_table(
   index="País",
   columns="Ano",
   values=metric_pivot,
   aggfunc="mean",
)

if metric_pivot in percent_cols:
   pivot_display = pivot.copy()
   pivot_display = (pivot_display * 100).round(1).astype(str) + "%"
else:
   pivot_display = pivot

st.write(f"Tabela dinâmica da métrica: {metric_pivot}")
st.dataframe(pivot_display, use_container_width=True)

csv_pivot = pivot.to_csv().encode("utf-8")
st.download_button(
   label="Baixar tabela dinâmica em CSV",
   data=csv_pivot,
   file_name=f"tabela_dinamica_{metric_pivot.replace(' ', '_')}.csv",
   mime="text/csv",
)

# ==========================================================
# 6A) ÍNDICE GERAL DE BEM ESTAR PERCEBIDO
# ==========================================================

st.subheader("Índice geral de bem estar percebido")

if ano_select == "Todos":
   ano_indice = df["Ano"].max()
   st.caption(f"Índice calculado para o ano mais recente disponível: {ano_indice}.")
else:
   ano_indice = ano_select

df_indice = df[df["Ano"] == ano_indice].copy()
df_indice = df_indice.dropna(subset=["Indice_Bem_Estar"])

df_indice = df_indice.sort_values("Indice_Bem_Estar", ascending=False)

top_n_indice = st.slider(
   "Quantos países mostrar no ranking do índice geral?",
   min_value=5,
   max_value=30,
   value=10,
)

st.write(
   "O índice geral combina Liberdade de escolhas, Expectativa de vida, "
   "Confiança no governo nacional e Percepções de corrupção (invertida), "
   "tudo normalizado entre 0 e 1."
)

df_indice_display = df_indice[
   [
      "País",
      "Indice_Bem_Estar",
      "Liberdade de escolhas",
      "Expectativa de vida",
      "Confiança no governo nacional",
      "Percepções de corrupção",
   ]
].copy()

df_indice_display = format_percent_cols(
   df_indice_display,
   ["Indice_Bem_Estar", "Liberdade de escolhas", "Confiança no governo nacional", "Percepções de corrupção"]
)

st.dataframe(
   df_indice_display.head(top_n_indice).reset_index(drop=True),
   use_container_width=True,
)

# ==========================================================
# 6B) RANKINGS ESPECÍFICOS LIBERDADE x MÉTRICA
# ==========================================================

st.subheader("Rankings específicos: liberdade combinada com uma métrica")

rank_metric = st.selectbox(
   "Escolha a métrica para construir o ranking",
   [
      "Expectativa de vida",
      "Confiança no governo nacional",
      "Percepções de corrupção (invertida)",
      "PIB per capita (US$) – razão Liberdade / PIB",
   ],
)

if ano_select == "Todos":
   ano_rank = df["Ano"].max()
   st.caption(f"Ranking calculado para o ano mais recente disponível: {ano_rank}.")
else:
   ano_rank = ano_select

df_rank = df[df["Ano"] == ano_rank].copy()

if rank_metric == "PIB per capita (US$) – razão Liberdade / PIB":
   df_rank = df_rank.dropna(subset=["Liberdade de escolhas", "PIB per capita (US$)"])
   df_rank = df_rank[df_rank["PIB per capita (US$)"] > 0]
   df_rank["Score_Ranking"] = (
      df_rank["Liberdade de escolhas"] / df_rank["PIB per capita (US$)"]
   )
   explicacao = "Score maior significa muita liberdade relativa ao nível de riqueza econômica."
   cols_show = [
      "País",
      "Liberdade de escolhas",
      "PIB per capita (US$)",
      "Score_Ranking",
   ]

   df_rank_display = df_rank[cols_show].copy()
   df_rank_display = format_percent_cols(df_rank_display, ["Liberdade de escolhas"])

else:
   if rank_metric == "Expectativa de vida":
      base_col = "Expectativa de vida"
   elif rank_metric == "Confiança no governo nacional":
      base_col = "Confiança no governo nacional"
   else:
      base_col = "Percepções de corrupção"

   df_rank = df_rank.dropna(subset=["Liberdade de escolhas", base_col])

   col_min = df_rank[base_col].min()
   col_max = df_rank[base_col].max()
   if col_max > col_min:
      metric_norm = (df_rank[base_col] - col_min) / (col_max - col_min)
   else:
      metric_norm = 0.5

   if base_col == "Percepções de corrupção":
      metric_norm = 1 - metric_norm
      explicacao = "Score maior significa alta liberdade combinada com baixa corrupção percebida."
   elif base_col == "Expectativa de vida":
      explicacao = "Score maior significa alta liberdade em países com maior expectativa de vida."
   else:
      explicacao = "Score maior significa alta liberdade em países com maior confiança no governo."

   df_rank["Score_Ranking"] = df_rank["Liberdade de escolhas"] * metric_norm

   cols_show = [
      "País",
      "Liberdade de escolhas",
      base_col,
      "Score_Ranking",
   ]

   df_rank_display = df_rank[cols_show].copy()
   # Liberdade sempre em %, base_col em % se for de 0 a 1
   percent_for_rank = ["Liberdade de escolhas"]
   if base_col in ["Confiança no governo nacional", "Percepções de corrupção"]:
      percent_for_rank.append(base_col)
   df_rank_display = format_percent_cols(df_rank_display, percent_for_rank)

df_rank_display = df_rank_display.sort_values("Score_Ranking", ascending=False)

top_n_rank = st.slider(
   "Quantos países mostrar no ranking específico?",
   min_value=5,
   max_value=30,
   value=10,
   key="slider_rank",
)

st.write(explicacao)

st.dataframe(
   df_rank_display.head(top_n_rank).reset_index(drop=True),
   use_container_width=True,
)

st.success("Dashboard carregado. Explore os filtros e rankings para investigar a relação entre liberdade e qualidade de vida.")
