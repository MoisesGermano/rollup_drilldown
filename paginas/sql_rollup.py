import streamlit as st
import pandas as pd

def mostrar_sql():
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("O Operador ROLLUP no SQL (A Automação dos Subtotais)")
    st.write("""
    No banco de dados, para gerar relatórios com esses resumos, usa-se o comando **ROLLUP**.
    
    * **Como funciona:** Em vez de você fazer três ou quatro consultas separadas para descobrir a venda por Ano, por Mês e por Dia, você roda o ROLLUP uma única vez.
    * Ele calcula tudo de forma inteligente de uma tacada só e entrega o relatório pronto com as linhas de detalhe, os subtotais e, no final de tudo, a linha do Total Geral.
    """)
    
    # --- EXEMPLO VISUAL: SIMULAÇÃO DO MYSQL WORKBENCH ---
    st.markdown("### 🖥️ Exemplo Prático: Execução no MySQL Workbench")
    
    # Cabeçalho da janela simulada
    st.markdown('<div class="workbench-header"><span>🐬 MySQL Workbench - [Query Editor]</span></div>', unsafe_allow_html=True)
    
    # Corpo da janela simulada contendo o código e o resultado
    with st.container():
        st.markdown('<div class="workbench-body">', unsafe_allow_html=True)
        
        st.code("""
-- Consultando vendas agrupadas com ROLLUP na hierarquia Ano -> Mês
SELECT 
    Ano, 
    Mes, 
    SUM(Valor_Vendas) AS Total_Vendas
FROM Vendas
GROUP BY Ano, Mes WITH ROLLUP;
        """, language="sql")
        
        st.markdown("**Grid de Resultados (Output):**", unsafe_allow_html=True)
        
        # DataFrame simulando o retorno real do banco com as linhas de subtotal e total geral (valores nulos)
        dados_vendas = {
            "Ano": ["2024", "2024", "2024", "2025", "2025", "2025", "NULL (Total Geral)"],
            "Mes": ["Janeiro", "Fevereiro", "NULL (Subtotal 2024)", "Janeiro", "Fevereiro", "NULL (Subtotal 2025)", "NULL"],
            "Total_Vendas": ["R$ 15.000", "R$ 18.000", "R$ 33.000", "R$ 20.000", "R$ 22.000", "R$ 42.000", "R$ 75.000"]
        }
        df = pd.DataFrame(dados_vendas)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.markdown('</div>', unsafe_allow_html=True)