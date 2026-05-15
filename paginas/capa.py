import streamlit as st

def mostrar_capa():
    # Logo Centralizado
    st.markdown('''
        <div class="logo-container">
            <img src="https://up.yimg.com/ib/th/id/OIP.KxJd185hgAvaySALzjpJMQHaBx?pid=Api&rs=1&c=1&qlt=95&w=495&h=118" width="100%"; height="90px" >
         </div>
    ''', unsafe_allow_html=True)
    
    # As linhas defasadas (Preto alinhado à esquerda, Vermelho alinhado à direita)
    st.markdown('''
        <div class="fatec-lines">
            <div class="line-black"></div>
            <div class="line-red"></div>
        </div>
    ''', unsafe_allow_html=True)
    
    # Título e Subtítulo em itálico
    st.markdown('<h1 class="title-presentation">Projeto Banco e Armazém de Dados</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="subtitle-presentation">Roll UP e Drill Down</h2>', unsafe_allow_html=True)
    
    # Estrutura de Alunos Centralizada
    st.markdown('''
        <div class="alunos-container">
            <div class="alunos-box">
                <p class="section-title-alunos">Alunos:</p>
                <div class="aluno-row"><span class="aluno-nome">Anderson Capelini</span> <span class="aluno-ra">RA: 2701352423043</span></div>
                <div class="aluno-row"><span class="aluno-nome">Marcelo Ramos</span> <span class="aluno-ra">RA: XXXXXXXXX</span></div>
                <div class="aluno-row"><span class="aluno-nome">Moisés Nascimento Germano</span> <span class="aluno-ra">RA: 2701352423043</span></div>
                <div class="aluno-row"><span class="aluno-nome">Victor Henrique</span> <span class="aluno-ra">RA: XXXXXXXXX</span></div>
                <div class="aluno-row"><span class="aluno-nome">Vitor Santos</span> <span class="aluno-ra">RA: XXXXXXXXX</span></div>
            </div>
        </div>
    ''', unsafe_allow_html=True)

    # Rodapé
    st.markdown('''
        <div class="footer-presentation">
            <p>Departamento de Tecnologia<br>2026</p>
        </div>
    ''', unsafe_allow_html=True)