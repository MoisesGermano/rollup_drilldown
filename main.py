import streamlit as st

# Importando o CSS
from estilos import aplicar_css_global

# Importando as páginas do projeto
from paginas.capa import mostrar_capa
from paginas.o_que_sao import mostrar_o_que_sao
from paginas.hierarquia import mostrar_hierarquia
from paginas.sql_rollup import mostrar_sql
from paginas.diferencas import mostrar_diferencas
from paginas.dashboards import mostrar_dashboards

# 1. Configuração da página em modo Wide (Largo)
st.set_page_config(
    page_title="Apresentação Fatec Cotia",
    layout="wide"
)

# 2. Aplica o arquivo de estilos global
aplicar_css_global()

# 3. Criação das 6 abas no topo (Navegador/Caderno Digital)
(aba_capa, aba_o_que_sao, aba_hierarquia, 
 aba_sql, aba_diferencas, aba_dashboards) = st.tabs([
    "O que são?", 
    "Hierarquia de Dados", 
    "ROLLUP no SQL", 
    "ROLLUP vs CUBE", 
    "Dashboards"
])

# 4. Roteamento: Coloca cada função dentro da sua aba correta
with aba_capa:
    mostrar_capa()
    
with aba_o_que_sao:
    mostrar_o_que_sao()
    
with aba_hierarquia:
    mostrar_hierarquia()
    
with aba_sql:
    mostrar_sql()
    
with aba_diferencas:
    mostrar_diferencas()
    
with aba_dashboards:
    mostrar_dashboards()