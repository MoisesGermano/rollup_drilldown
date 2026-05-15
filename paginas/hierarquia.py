import streamlit as st
import streamlit.components.v1 as components

def mostrar_hierarquia():
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("O que é uma \"Hierarquia\" de Dados?")
    st.markdown("#### *Para que o Zoom funcione, os dados precisam estar organizados como uma escada, onde cada degrau de cima é o resumo do degrau de baixo.*")
    st.write("")
    
    st.markdown("### Os três exemplos mais comuns no mundo dos negócios são:")
    st.latex(r"\text{Tempo: } Ano \rightarrow Trimestre \rightarrow Mês \rightarrow Dia")
    st.latex(r"\text{Geografia: } País \rightarrow Estado \rightarrow Cidade \rightarrow Bairro")
    st.latex(r"\text{Produto: } Categoria \text{ (ex: Eletrônicos)} \rightarrow Subcategoria \text{ (ex: Smartphones)} \rightarrow Modelo")
    
    st.write("<br>", unsafe_allow_html=True)
    
    # Caixa de alerta customizada imune ao Dark Mode do Streamlit
    st.markdown("""
        <div style="background-color: #fff3cd; color: #856404; padding: 20px; border-radius: 8px; border-left: 6px solid #ffeeba; font-size: 18px;">
            <strong>⚠️ Nota de Atenção:</strong> Na engrenagem do sistema, é preciso cuidado com nomes repetidos. 
            Por exemplo, existem cidades chamadas "San Jose" na Califórnia e em Porto Rico. 
            O sistema deve usar códigos (IDs) para não somar os dados das duas cidades achando que é a mesma.
        </div>
    """, unsafe_allow_html=True)

    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("### 🖱️ Demonstração Interativa (Clique para dar Zoom)")
    
    # Caixa flutuante interativa com HTML/JS
    components.html("""
    <style>
        body { 
            font-family: 'Arial', sans-serif; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            margin: 0; 
            padding: 20px;
        }
        .floating-box {
            background: #ffffff;
            border: 2px solid #B22222;
            border-radius: 12px;
            box-shadow: 0 15px 30px rgba(0,0,0,0.15);
            padding: 30px;
            text-align: center;
            width: 450px;
            transition: all 0.3s ease;
        }
        .title-text { 
            font-size: 22px; 
            font-weight: bold; 
            color: #333; 
            margin-bottom: 20px; 
        }
        .btn-year {
            background-color: #B22222; 
            color: white; 
            border: none; 
            padding: 20px 40px; 
            font-size: 36px; 
            font-weight: bold;
            border-radius: 10px; 
            cursor: pointer; 
            width: 100%; 
            transition: background 0.3s, transform 0.1s;
        }
        .btn-year:hover { 
            background-color: #8B0000; 
            transform: scale(1.02);
        }
        
        .grid-months { 
            display: grid; 
            grid-template-columns: repeat(3, 1fr); 
            gap: 12px; 
        }
        .btn-month {
            background-color: #f0f2f5; 
            border: 1px solid #ccc; 
            padding: 15px; 
            font-size: 16px; 
            font-weight: bold;
            border-radius: 8px; 
            cursor: pointer; 
            transition: all 0.2s;
        }
        .btn-month:hover { 
            background-color: #1E90FF; 
            color: white; 
            border-color: #1E90FF; 
            transform: scale(1.05);
        }
        
        .grid-days { 
            display: grid; 
            grid-template-columns: repeat(7, 1fr); 
            gap: 6px; 
            margin-top: 15px;
        }
        .day-cell {
            background-color: #f9f9f9; 
            border: 1px solid #ddd; 
            padding: 10px 0; 
            font-size: 14px; 
            border-radius: 4px; 
            text-align: center;
            cursor: default;
        }
        .day-cell:hover {
            background-color: #e2e8f0;
        }
        
        .back-btn {
            background-color: transparent; 
            color: #666; 
            border: none; 
            text-decoration: underline; 
            margin-top: 25px; 
            cursor: pointer; 
            font-size: 15px;
        }
        .back-btn:hover { 
            color: #B22222; 
        }
        .hint {
            color: #777; 
            font-size: 13px; 
            margin-top: 15px;
        }
    </style>

    <div class="floating-box" id="main-box">
        <div id="level-year">
            <div class="title-text">Hierarquia de Tempo</div>
            <button class="btn-year" onclick="showMonths()">2026</button>
            <p class="hint">👆 Clique no ano para fazer o Drill Down (Ver Meses)</p>
        </div>

        <div id="level-month" style="display: none;">
            <div class="title-text">Ano: 2026</div>
            <div class="grid-months">
                <button class="btn-month" onclick="showDays('Janeiro', 31)">Jan</button>
                <button class="btn-month" onclick="showDays('Fevereiro', 28)">Fev</button>
                <button class="btn-month" onclick="showDays('Março', 31)">Mar</button>
                <button class="btn-month" onclick="showDays('Abril', 30)">Abr</button>
                <button class="btn-month" onclick="showDays('Maio', 31)">Mai</button>
                <button class="btn-month" onclick="showDays('Junho', 30)">Jun</button>
                <button class="btn-month" onclick="showDays('Julho', 31)">Jul</button>
                <button class="btn-month" onclick="showDays('Agosto', 31)">Ago</button>
                <button class="btn-month" onclick="showDays('Setembro', 30)">Set</button>
                <button class="btn-month" onclick="showDays('Outubro', 31)">Out</button>
                <button class="btn-month" onclick="showDays('Novembro', 30)">Nov</button>
                <button class="btn-month" onclick="showDays('Dezembro', 31)">Dez</button>
            </div>
            <p class="hint">👆 Clique em um mês para fazer o Drill Down (Ver Dias)</p>
            <button class="back-btn" onclick="goBack('year')">⬅ Fazer Roll Up (Voltar para Ano)</button>
        </div>

        <div id="level-day" style="display: none;">
            <div class="title-text" id="day-title">Mês</div>
            <div class="grid-days" id="days-container"></div>
            <button class="back-btn" onclick="goBack('month')">⬅ Fazer Roll Up (Voltar para Meses)</button>
        </div>
    </div>

    <script>
        // Função para mostrar os meses (Zoom In Nível 1)
        function showMonths() {
            document.getElementById('level-year').style.display = 'none';
            document.getElementById('level-day').style.display = 'none';
            document.getElementById('level-month').style.display = 'block';
        }

        // Função para mostrar os dias dependendo do mês clicado (Zoom In Nível 2)
        function showDays(monthName, daysCount) {
            document.getElementById('level-year').style.display = 'none';
            document.getElementById('level-month').style.display = 'none';
            document.getElementById('level-day').style.display = 'block';
            
            document.getElementById('day-title').innerText = monthName + ' de 2026';
            
            let daysHtml = '';
            for(let i=1; i<=daysCount; i++) {
                daysHtml += `<div class="day-cell">${i}</div>`;
            }
            document.getElementById('days-container').innerHTML = daysHtml;
        }

        // Função para voltar os níveis (Zoom Out / Roll Up)
        function goBack(level) {
            if(level === 'year') {
                document.getElementById('level-month').style.display = 'none';
                document.getElementById('level-day').style.display = 'none';
                document.getElementById('level-year').style.display = 'block';
            } else if (level === 'month') {
                document.getElementById('level-day').style.display = 'none';
                document.getElementById('level-month').style.display = 'block';
            }
        }
    </script>
    """, height=500)