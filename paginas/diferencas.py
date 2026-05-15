import streamlit as st
import streamlit.components.v1 as components

def mostrar_diferencas():
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("A Diferença entre ROLLUP, CUBE e GROUPING SETS")
    st.markdown("#### *O banco de dados oferece três formas de resumir as coisas, dependendo da sua necessidade:*")
    st.write("")
    
    st.markdown(r"""
    * **ROLLUP:** Segue uma linha reta e hierárquica ($Ano \rightarrow Mês \rightarrow Dia$). Só faz sentido nessa ordem.
    * **CUBE:** Mistura todas as combinações possíveis, mesmo que não haja uma hierarquia. Ele cruza, por exemplo, "Cor do Carro" com "Loja" com "Forma de Pagamento" para te dar todas as estatísticas possíveis.
    * **GROUPING SETS:** É o "filtro sob medida". Se você quer apenas o total por Cidade e o Total Geral, pulando o subtotal por Estado para o relatório ficar mais leve, você avisa o sistema usando essa função.
    """)
    
    st.write("<br>", unsafe_allow_html=True)
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("🧊 Exemplo 1: ROLLUP vs CUBE")
        st.write("Veja como o **CUBE** descobre subtotais que o ROLLUP ignora (por cruzar tudo com tudo).")
        
        components.html("""
        <style>
            body { font-family: 'Arial', sans-serif; padding: 10px; margin: 0; color: #333; }
            .box { border: 1px solid #ddd; border-radius: 8px; padding: 15px; background: #fff; box-shadow: 0 4px 8px rgba(0,0,0,0.05); }
            .btn-group { display: flex; gap: 10px; margin-bottom: 15px; }
            .btn-sql { flex: 1; padding: 10px; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; transition: 0.2s; background-color: #f0f2f5; color: #333; border: 1px solid #ccc; }
            .btn-sql:hover { background-color: #e2e8f0; }
            .btn-sql.active { background-color: #1E90FF; color: white; border-color: #1E90FF; }
            
            table { width: 100%; border-collapse: collapse; text-align: center; font-size: 14px; }
            th { background-color: #f8f9fa; color: #555; padding: 8px; border-bottom: 2px solid #ddd; }
            td { padding: 8px; border-bottom: 1px solid #eee; }
            .null-val { color: #aaa; font-style: italic; }
            .subtotal { background-color: #f4f4f4; font-weight: bold; }
            .cube-extra { background-color: #fff3cd; font-weight: bold; color: #856404; animation: highlight 1s ease-in-out; }
            .total { background-color: #e2e8f0; font-weight: bold; color: #B22222; }
            
            @keyframes highlight { 0% { background-color: #ffeeba; transform: scale(1.02); } 100% { background-color: #fff3cd; transform: scale(1); } }
        </style>

        <div class="box">
            <div class="btn-group">
                <button class="btn-sql active" id="btnRollup" onclick="showTable('rollup')">Gerar ROLLUP</button>
                <button class="btn-sql" id="btnCube" onclick="showTable('cube')">Gerar CUBE</button>
            </div>
            
            <div id="table-container">
                </div>
            <p id="obs-text" style="font-size: 12px; color: #777; text-align: center; margin-top: 15px;">
                O ROLLUP calcula as vendas por Loja, e o Total Geral.
            </p>
        </div>

        <script>
            const htmlRollup = `
                <table>
                    <tr><th>Loja</th><th>Cor do Carro</th><th>Vendas</th></tr>
                    <tr><td>Matriz</td><td>Preto</td><td>R$ 100</td></tr>
                    <tr><td>Matriz</td><td>Branco</td><td>R$ 150</td></tr>
                    <tr class="subtotal"><td>Matriz</td><td class="null-val">NULL (Subtotal)</td><td>R$ 250</td></tr>
                    <tr><td>Filial</td><td>Preto</td><td>R$ 200</td></tr>
                    <tr class="subtotal"><td>Filial</td><td class="null-val">NULL (Subtotal)</td><td>R$ 200</td></tr>
                    <tr class="total"><td class="null-val">NULL</td><td class="null-val">NULL (Total Geral)</td><td>R$ 450</td></tr>
                </table>
            `;

            const htmlCube = `
                <table>
                    <tr><th>Loja</th><th>Cor do Carro</th><th>Vendas</th></tr>
                    <tr><td>Matriz</td><td>Preto</td><td>R$ 100</td></tr>
                    <tr><td>Matriz</td><td>Branco</td><td>R$ 150</td></tr>
                    <tr class="subtotal"><td>Matriz</td><td class="null-val">NULL (Subtotal Loja)</td><td>R$ 250</td></tr>
                    <tr><td>Filial</td><td>Preto</td><td>R$ 200</td></tr>
                    <tr class="subtotal"><td>Filial</td><td class="null-val">NULL (Subtotal Loja)</td><td>R$ 200</td></tr>
                    <tr class="cube-extra"><td class="null-val">NULL (Subtotal Cor)</td><td>Preto</td><td>R$ 300 👈 Novo!</td></tr>
                    <tr class="cube-extra"><td class="null-val">NULL (Subtotal Cor)</td><td>Branco</td><td>R$ 150 👈 Novo!</td></tr>
                    <tr class="total"><td class="null-val">NULL</td><td class="null-val">NULL (Total Geral)</td><td>R$ 450</td></tr>
                </table>
            `;

            function showTable(type) {
                document.getElementById('btnRollup').classList.remove('active');
                document.getElementById('btnCube').classList.remove('active');
                
                if(type === 'rollup') {
                    document.getElementById('btnRollup').classList.add('active');
                    document.getElementById('table-container').innerHTML = htmlRollup;
                    document.getElementById('obs-text').innerText = "O ROLLUP calcula os subtotais seguindo apenas a ordem Loja -> Cor.";
                } else {
                    document.getElementById('btnCube').classList.add('active');
                    document.getElementById('table-container').innerHTML = htmlCube;
                    document.getElementById('obs-text').innerHTML = "O CUBE vai além: ele cruza os dados de trás pra frente e descobre o <b>Total de Carros Pretos e Brancos</b> somando todas as lojas (linhas em amarelo).";
                }
            }
            
            // Iniciar com Rollup
            showTable('rollup');
        </script>
        """, height=420)

    with col_right:
        st.subheader("🎯 Exemplo 2: GROUPING SETS")
        st.write("O relatório sob medida. Peça ao banco de dados para calcular **apenas** o que você marcar.")
        
        components.html("""
        <style>
            body { font-family: 'Arial', sans-serif; padding: 10px; margin: 0; color: #333; }
            .box { border: 1px solid #ddd; border-radius: 8px; padding: 15px; background: #fff; box-shadow: 0 4px 8px rgba(0,0,0,0.05); }
            
            .checkbox-group { display: flex; flex-direction: column; gap: 8px; margin-bottom: 15px; background: #f8f9fa; padding: 10px; border-radius: 6px; border: 1px solid #eee; }
            .checkbox-label { cursor: pointer; font-size: 14px; display: flex; align-items: center; gap: 8px; font-weight: bold; }
            
            table { width: 100%; border-collapse: collapse; text-align: center; font-size: 14px; }
            th { background-color: #B22222; color: white; padding: 8px; border-bottom: 2px solid #ddd; }
            td { padding: 8px; border-bottom: 1px solid #eee; }
            .null-val { color: #aaa; font-style: italic; }
            .row-estado { background-color: #e2e8f0; font-weight: bold; color: #333; }
            .row-total { background-color: #2b2b2b; font-weight: bold; color: white; }
        </style>

        <div class="box">
            <div style="font-size: 13px; color: #555; margin-bottom: 5px;">Selecione os agrupamentos desejados:</div>
            <div class="checkbox-group">
                <label class="checkbox-label">
                    <input type="checkbox" id="chkEstado" onchange="updateSets()" checked> 
                    Incluir Subtotal por Estado
                </label>
                <label class="checkbox-label">
                    <input type="checkbox" id="chkTotal" onchange="updateSets()"> 
                    Incluir Total Geral (Pulando o resto)
                </label>
            </div>
            
            <table>
                <thead>
                    <tr><th>Estado</th><th>Cidade</th><th>Vendas</th></tr>
                </thead>
                <tbody id="sets-body">
                    </tbody>
            </table>
        </div>

        <script>
            const dataBase = `
                <tr><td>SP</td><td>Cotia</td><td>R$ 10.000</td></tr>
                <tr><td>SP</td><td>Osasco</td><td>R$ 8.000</td></tr>
                <tr><td>RJ</td><td>Niterói</td><td>R$ 5.000</td></tr>
            `;
            const subtotalEstado = `
                <tr class="row-estado"><td>SP</td><td class="null-val">NULL</td><td>R$ 18.000</td></tr>
                <tr class="row-estado"><td>RJ</td><td class="null-val">NULL</td><td>R$ 5.000</td></tr>
            `;
            const totalGeral = `
                <tr class="row-total"><td class="null-val">NULL</td><td class="null-val">NULL</td><td>R$ 23.000</td></tr>
            `;

            function updateSets() {
                let showEstado = document.getElementById('chkEstado').checked;
                let showTotal = document.getElementById('chkTotal').checked;
                
                let finalHtml = dataBase; // Sempre mostra os detalhes
                
                if(showEstado) finalHtml += subtotalEstado;
                if(showTotal) finalHtml += totalGeral;
                
                document.getElementById('sets-body').innerHTML = finalHtml;
            }
            
            // Inicia a tabela
            updateSets();
        </script>
        """, height=420)