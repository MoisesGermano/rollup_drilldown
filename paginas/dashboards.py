import streamlit as st
import streamlit.components.v1 as components

def mostrar_dashboards():
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("A Diferença no Painel (Dashboard): Drill Down vs. Drill Through")
    st.markdown("#### *Quando você está olhando para os gráficos em uma tela de Business Intelligence (como Power BI ou Tableau), a interatividade muda de nome conforme o comportamento:*")
    st.write("")
    
    col_down, col_through = st.columns(2)
    
    with col_down:
        st.info("### 📉 Drill Down")
        st.write("""
        **Ocorre dentro do mesmo gráfico.** Você clica na barra do ano "2026" e o gráfico se transforma sozinho, mostrando barras menores (uma para cada trimestre ou mês).
        """)
        
        components.html("""
        <style>
            body { font-family: 'Arial', sans-serif; padding: 10px; margin: 0; color: #333; }
            .box { border: 1px solid #ddd; border-radius: 8px; padding: 15px; background: #fff; box-shadow: 0 4px 8px rgba(0,0,0,0.05); height: 320px; display: flex; flex-direction: column;}
            .chart-area { flex-grow: 1; display: flex; align-items: flex-end; justify-content: center; gap: 15px; padding-bottom: 20px; border-bottom: 2px solid #eee; margin-bottom: 15px; }
            
            .bar { background-color: #1E90FF; width: 80px; text-align: center; color: white; font-weight: bold; padding-top: 10px; border-radius: 4px 4px 0 0; cursor: pointer; transition: 0.3s; box-shadow: 0 2px 5px rgba(0,0,0,0.2); }
            .bar:hover { background-color: #0066cc; transform: scaleY(1.05); }
            .bar-small { background-color: #4682B4; width: 50px; font-size: 12px; }
            
            .btn-back { background-color: #f0f2f5; color: #333; border: 1px solid #ccc; padding: 10px; border-radius: 6px; cursor: pointer; font-weight: bold; width: 100%; transition: 0.2s; }
            .btn-back:hover { background-color: #e2e8f0; }
            .hint { font-size: 13px; color: #777; text-align: center; margin-bottom: 10px; }
        </style>

        <div class="box">
            <div class="hint" id="dd-title">Visão Anual (Clique na barra do Ano)</div>
            
            <div class="chart-area" id="chart-year">
                <div class="bar" style="height: 180px;" onclick="doDrillDown()" title="Clique para fazer Drill Down">2026<br><br>🖱️</div>
            </div>

            <div class="chart-area" id="chart-quarters" style="display: none;">
                <div class="bar bar-small" style="height: 60px;">Tri 1</div>
                <div class="bar bar-small" style="height: 120px;">Tri 2</div>
                <div class="bar bar-small" style="height: 90px;">Tri 3</div>
                <div class="bar bar-small" style="height: 180px;">Tri 4</div>
            </div>
            
            <button class="btn-back" id="btn-up" style="display: none;" onclick="undoDrillDown()">🔼 Fazer Roll Up (Voltar ao Ano)</button>
        </div>

        <script>
            function doDrillDown() {
                document.getElementById('chart-year').style.display = 'none';
                document.getElementById('chart-quarters').style.display = 'flex';
                document.getElementById('btn-up').style.display = 'block';
                document.getElementById('dd-title').innerText = "Visão Trimestral (O gráfico se dividiu em 4)";
            }
            function undoDrillDown() {
                document.getElementById('chart-quarters').style.display = 'none';
                document.getElementById('chart-year').style.display = 'flex';
                document.getElementById('btn-up').style.display = 'none';
                document.getElementById('dd-title').innerText = "Visão Anual (Clique na barra do Ano)";
            }
        </script>
        """, height=380)

    with col_through:
        st.success("### 🚀 Drill Through")
        st.write("""
        **É uma viagem entre páginas.** Você clica com o botão direito na região "Sudeste" e escolhe "Ver detalhes". O sistema te leva para uma página totalmente nova, cheia de outras tabelas e mapas.
        """)
        
        components.html("""
        <style>
            body { font-family: 'Arial', sans-serif; padding: 10px; margin: 0; color: #333; }
            .box { border: 1px solid #ddd; border-radius: 8px; padding: 15px; background: #fff; box-shadow: 0 4px 8px rgba(0,0,0,0.05); height: 320px; position: relative; overflow: hidden; }
            
            /* Página Principal */
            .page-main { display: flex; flex-direction: column; gap: 10px; height: 100%; transition: 0.3s; }
            .card { background: #f8f9fa; border: 1px solid #eee; border-radius: 6px; padding: 15px; text-align: center; }
            .card-interactive { background: #e8f5e9; border: 1px solid #c8e6c9; cursor: pointer; transition: 0.2s; }
            .card-interactive:hover { background: #c8e6c9; transform: scale(1.02); }
            
            /* Página Detalhada (A Nova Tela) */
            .page-detail { position: absolute; top: 0; left: 100%; width: 100%; height: 100%; background: #2b2b2b; color: white; padding: 15px; transition: left 0.4s ease-in-out; box-sizing: border-box; }
            .page-detail.active { left: 0; }
            
            .grid-detail { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 15px; }
            .mini-chart { background: #444; border-radius: 4px; padding: 20px; text-align: center; font-size: 12px; }
            
            .btn-back { background-color: #B22222; color: white; border: none; padding: 8px; border-radius: 4px; cursor: pointer; font-size: 12px; font-weight: bold; width: 100%; margin-top: 15px;}
            .btn-back:hover { background-color: #8B0000; }
            .hint { font-size: 13px; color: #777; text-align: center; margin-bottom: 10px; }
        </style>

        <div class="box">
            <div class="page-main" id="page-1">
                <div class="hint">Dashboard Global (Página 1)</div>
                <div class="card">Região Sul: R$ 400.000</div>
                <div class="card">Região Norte: R$ 250.000</div>
                <div class="card card-interactive" onclick="doDrillThrough()" title="Botão Direito -> Drill Through">
                    <b>Região Sudeste: R$ 900.000</b><br>
                    <span style="font-size: 12px; color: #2e7d32;">(Clique para viajar de página) 🚀</span>
                </div>
            </div>

            <div class="page-detail" id="page-2">
                <h4 style="margin: 0; color: #4CAF50;">📍 Detalhes: Sudeste</h4>
                <p style="font-size: 11px; margin-top: 5px; color: #aaa;">Você foi levado para uma aba completamente nova!</p>
                
                <div class="grid-detail">
                    <div class="mini-chart">Tabela Cidades<br>📊</div>
                    <div class="mini-chart">Mapa de Calor<br>🗺️</div>
                    <div class="mini-chart" style="grid-column: span 2;">Top Produtos<br>📈</div>
                </div>
                
                <button class="btn-back" onclick="undoDrillThrough()">⬅ Voltar para a Página Principal</button>
            </div>
        </div>

        <script>
            function doDrillThrough() {
                // Adiciona a classe que faz a página 2 deslizar para a tela
                document.getElementById('page-2').classList.add('active');
            }
            function undoDrillThrough() {
                // Remove a classe para a página 2 voltar para a direita
                document.getElementById('page-2').classList.remove('active');
            }
        </script>
        """, height=380)