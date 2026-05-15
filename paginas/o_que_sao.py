import streamlit as st
import streamlit.components.v1 as components

def mostrar_o_que_sao():
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("O que são Roll Up e Drill Down? (O Efeito 'Zoom')")
    st.markdown("#### *Esses dois termos representam a direção para onde você está olhando os seus dados.*")
    st.write("")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("🔼 Roll Up (Dar \"Zoom Out\")")
        st.write("""
        Significa subir o nível, juntar os pedacinhos e olhar o quadro geral. 
        É quando você pega as vendas de cada dia e soma tudo para ver o total do ano. 
        Serve para diretores e chefes que precisam de resumos rápidos.
        """)
        
        st.markdown("#### Exemplo Visual: Roll Up")
        
        components.html("""
        <style>
            body { font-family: 'Arial', sans-serif; padding: 10px; margin: 0; color: #333; }
            .box { border: 1px solid #ddd; border-radius: 8px; padding: 15px; background: #fff; box-shadow: 0 4px 8px rgba(0,0,0,0.05); }
            table { width: 100%; border-collapse: collapse; text-align: center; margin-bottom: 15px; }
            th { background-color: #f8f9fa; color: #555; padding: 10px; border-bottom: 2px solid #ddd; }
            td { padding: 10px; border-bottom: 1px solid #eee; }
            .btn-rollup { background-color: #1E90FF; color: white; border: none; padding: 12px; width: 100%; border-radius: 6px; font-weight: bold; cursor: pointer; transition: 0.2s; }
            .btn-rollup:hover { background-color: #0066cc; }
            .btn-drill { background-color: #6c757d; color: white; border: none; padding: 12px; width: 100%; border-radius: 6px; font-weight: bold; cursor: pointer; transition: 0.2s; }
            .btn-drill:hover { background-color: #5a6268; }
            .hint { font-size: 13px; color: #777; text-align: center; margin-bottom: 10px; }
        </style>

        <div class="box">
            <div id="rollup-detail">
                <div class="hint">Tabela de Vendas Diárias (Nível Dia)</div>
                <table>
                    <tr><th>Data</th><th>Região</th><th>Vendas</th></tr>
                    <tr><td>01/01/2026</td><td>Norte</td><td>R$ 100</td></tr>
                    <tr><td>02/01/2026</td><td>Norte</td><td>R$ 150</td></tr>
                    <tr><td>03/01/2026</td><td>Sul</td><td>R$ 200</td></tr>
                    <tr><td>04/01/2026</td><td>Sul</td><td>R$ 250</td></tr>
                </table>
                <button class="btn-rollup" onclick="fazerRollup()">🔼 Fazer Roll Up (Agrupar por Região)</button>
            </div>

            <div id="rollup-grouped" style="display: none;">
                <div class="hint">Tabela Consolidada (Nível Região)</div>
                <table>
                    <tr><th>Região</th><th>Total de Vendas</th></tr>
                    <tr><td>Norte</td><td><b>R$ 250</b></td></tr>
                    <tr><td>Sul</td><td><b>R$ 450</b></td></tr>
                </table>
                <button class="btn-drill" onclick="desfazerRollup()">🔽 Desfazer (Ver Detalhes Diários)</button>
            </div>
        </div>

        <script>
            function fazerRollup() {
                document.getElementById('rollup-detail').style.display = 'none';
                document.getElementById('rollup-grouped').style.display = 'block';
            }
            function desfazerRollup() {
                document.getElementById('rollup-grouped').style.display = 'none';
                document.getElementById('rollup-detail').style.display = 'block';
            }
        </script>
        """, height=350)

    with col_right:
        st.subheader("🔽 Drill Down (Dar \"Zoom In\")")
        st.write("""
        Significa "perfurar" ou detalhar. É quando você clica em um número consolidado para ver o que tem dentro dele. 
        Se o relatório diz que a empresa perdeu dinheiro no mês, você faz um Drill Down para descobrir qual produto ou filial causou o prejuízo.
        """)
        
        st.markdown("#### Exemplo Visual: Drill Down")
        
        components.html("""
        <style>
            body { font-family: 'Arial', sans-serif; padding: 10px; margin: 0; color: #333; }
            .box { border: 1px solid #ddd; border-radius: 8px; padding: 15px; background: #fff; box-shadow: 0 4px 8px rgba(0,0,0,0.05); }
            table { width: 100%; border-collapse: collapse; text-align: center; margin-bottom: 15px; }
            th { background-color: #f8f9fa; color: #555; padding: 10px; border-bottom: 2px solid #ddd; }
            td { padding: 10px; border-bottom: 1px solid #eee; }
            
            /* Célula clicável do Drill Down */
            .drill-link { color: #B22222; font-weight: bold; background-color: #ffeeee; cursor: pointer; text-decoration: underline; transition: 0.2s; border-radius: 4px;}
            .drill-link:hover { background-color: #ffcccc; color: #8B0000; }
            
            .btn-rollup { background-color: #1E90FF; color: white; border: none; padding: 12px; width: 100%; border-radius: 6px; font-weight: bold; cursor: pointer; transition: 0.2s; }
            .btn-rollup:hover { background-color: #0066cc; }
            .hint { font-size: 13px; color: #777; text-align: center; margin-bottom: 10px; }
            .negative { color: #B22222; font-weight: bold; }
        </style>

        <div class="box">
            <div id="drill-summary">
                <div class="hint">Visão Geral (O diretor vê prejuízo no Sul)</div>
                <table>
                    <tr><th>Mês</th><th>Região</th><th>Lucro Total</th></tr>
                    <tr><td>Jan</td><td>Norte</td><td>R$ 5.000</td></tr>
                    <tr><td>Jan</td><td>Sul</td><td class="drill-link" onclick="fazerDrilldown()" title="Clique para investigar!">R$ -2.000</td></tr>
                </table>
                <p style="font-size: 12px; text-align: center; color: #B22222;">👆 Clique no valor "-2.000" para investigar de onde veio o prejuízo!</p>
            </div>

            <div id="drill-detail" style="display: none;">
                <div class="hint">Drill Down (Detalhando as lojas do Sul)</div>
                <table>
                    <tr><th>Loja</th><th>Lucro</th></tr>
                    <tr><td>Curitiba (PR)</td><td>R$ 1.500</td></tr>
                    <tr><td>Porto Alegre (RS)</td><td class="negative">R$ -4.000</td></tr>
                    <tr><td>Florianópolis (SC)</td><td>R$ 500</td></tr>
                    <tr style="background-color: #f4f4f4;"><td><b>Total (Sul)</b></td><td class="negative">R$ -2.000</td></tr>
                </table>
                <button class="btn-rollup" onclick="desfazerDrilldown()">🔼 Fazer Roll Up (Voltar ao Resumo)</button>
            </div>
        </div>

        <script>
            function fazerDrilldown() {
                document.getElementById('drill-summary').style.display = 'none';
                document.getElementById('drill-detail').style.display = 'block';
            }
            function desfazerDrilldown() {
                document.getElementById('drill-detail').style.display = 'none';
                document.getElementById('drill-summary').style.display = 'block';
            }
        </script>
        """, height=350)