import streamlit as st

def aplicar_css_global():
    st.markdown("""
        <style>
            /* Desativa o cabeçalho padrão do Streamlit */
            header[data-testid="stHeader"] {
                display: none !important;
            }
            
            /* Oculta a barra lateral esquerda */
            [data-testid="stSidebar"] {
                display: none !important;
            }
            
            /* Remove o fundo escuro do app e bota branco em tudo */
            .stApp {
                background-color: #ffffff !important;
                color: black;
            }
            
            /* Zera os paddings e faz o container ocupar 100% das laterais da tela */
            .block-container {
                padding-top: 0px !important;
                padding-bottom: 0px !important;
                padding-left: 40px !important;
                padding-right: 40px !important;
                max-width: 100% !important;
            }
            
            /* =======================================================
               NAVEGADOR FIXO NO TOPO (À PROVA DE FALHAS)
               ======================================================= */
            
            /* Prega o menu no teto do navegador (Viewport) */
            div[data-baseweb="tab-list"] {
                position: fixed !important;
                top: 0px !important;
                left: 0px !important;
                width: 100vw !important; /* Ocupa a largura inteira da tela */
                z-index: 999999 !important; /* Fica acima de todas as tabelas e gráficos */
                background-color: #ffffff !important; /* Fundo branco para esconder o conteúdo passando */
                padding: 15px 40px 10px 40px !important;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05) !important; /* Sombra leve para dar efeito flutuante */
                display: flex !important;
                justify-content: center !important; /* Centraliza as abas na tela */
                gap: 6px !important;
            }

            /* Empurra todo o conteúdo do site para baixo para não nascer escondido atrás das abas */
            div[data-testid="stTabs"] > div[role="tabpanel"] {
                margin-top: 80px !important; 
            }

            /* Estilo das abas */
            button[data-baseweb="tab"] {
                font-size: 15px !important;
                font-weight: 600 !important;
                padding: 10px 18px !important;
                background-color: #333333 !important;
                color: #ffffff !important;
                border-radius: 8px 8px 0 0 !important;
                border: none !important;
                transition: all 0.2s ease-in-out !important;
            }

            button[data-baseweb="tab"]:hover {
                background-color: #555555 !important;
                color: #ffffff !important;
            }

            button[data-baseweb="tab"][aria-selected="true"] {
                background-color: #B22222 !important;
                color: #ffffff !important;
                transform: scaleY(1.05);
                transform-origin: bottom;
            }

            div[data-baseweb="tab-highlight"] {
                display: none !important;
            }

            /* =======================================================
               ESTILOS DA CAPA (IDENTICO À IMAGEM DA FATEC)
               ======================================================= */
               
            .logo-container { text-align: center; padding-top: 20px; margin-bottom: 20px; }
            
            /* Linhas defasadas */
            .fatec-lines { margin-bottom: 40px; margin-top: 20px; }
            .line-black { height: 8px; background-color: #000000; width: 85%; margin: 0 auto 4px 0; }
            .line-red { height: 8px; background-color: #FF0000; width: 85%; margin: 0 0 0 auto; }
            
            .title-presentation { font-family: 'Arial', sans-serif; font-size: 42px; font-weight: bold; font-style: italic; text-transform: uppercase; text-align: center; margin-bottom: 5px; margin-top: 10px; color: #000; }
            .subtitle-presentation { font-family: 'Arial', sans-serif; font-size: 28px; text-align: center; color: #333; margin-bottom: 50px; font-style: italic; }
            
            .alunos-container { display: flex; justify-content: center; margin-bottom: 40px; }
            .alunos-box { width: 60%; } /* Controla a largura da lista para não ficar espalhada */
            .section-title-alunos { font-family: 'Arial', sans-serif; font-size: 24px; font-style: italic; font-weight: bold; color: #000000; margin-bottom: 15px; }
            .aluno-row { display: flex; justify-content: space-between; font-family: 'Arial', sans-serif; font-size: 22px; color: #000000; margin-bottom: 8px; }
            .aluno-nome { font-style: italic; }
            .aluno-ra { font-weight: bold; font-style: italic; }
            
            .footer-presentation { font-family: 'Arial', sans-serif; font-size: 28px; font-style: italic; color: #000000; text-align: center; margin-top: 50px; line-height: 1.4; }
            
            /* CSS do MySQL Workbench */
            .workbench-header { background-color: #2b2b2b; color: #ffffff; padding: 8px 15px; font-family: 'Segoe UI', Tahoma, sans-serif; font-size: 14px; border-radius: 6px 6px 0 0; display: flex; align-items: center; gap: 10px; }
            .workbench-body { background-color: #ffffff; border: 1px solid #2b2b2b; border-radius: 0 0 6px 6px; padding: 15px; margin-bottom: 20px; }
        </style>
    """, unsafe_allow_html=True)