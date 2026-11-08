import streamlit as st
import pandas as pd
from profiles import FILMES_DREAMWORKS, FILMES_METADATA, PERFIS_FICTICIOS
from recommender import rankear_perfis, calcular_similaridade

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="DreamMatch - Recomendador DreamWorks (D&C)",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ESTILIZAÇÃO CSS CUSTOMIZADA ---
st.markdown("""
<style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #FF4B4B, #FF8533, #FFD000);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #888888;
        font-size: 1.1rem;
        margin-top: 0px;
        margin-bottom: 25px;
    }
    .winner-card {
        background: linear-gradient(135deg, rgba(255, 75, 75, 0.15) 0%, rgba(255, 133, 51, 0.15) 100%);
        border: 2px solid #FF4B4B;
        border-radius: 12px;
        padding: 24px;
        text-align: center;
        margin-bottom: 24px;
    }
    .profile-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 12px;
    }
    .movie-pill {
        display: inline-block;
        padding: 4px 10px;
        background-color: #262730;
        border-radius: 15px;
        margin: 2px;
        font-size: 0.85rem;
    }
    /* Estilização dos botões de subir e descer para preencherem o espaço */
    div[data-testid="stColumn"] div.stButton > button {
        width: 100% !important;
        min-height: 40px !important;
        background: #2b2d35 !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 8px !important;
        padding: 2px 6px !important;
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        transition: all 0.2s ease !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    div[data-testid="stColumn"] div.stButton > button p {
        font-size: 1.15rem !important;
        margin: 0 !important;
        line-height: 1 !important;
    }
    div[data-testid="stColumn"] div.stButton > button:hover:not(:disabled) {
        background: #FF4B4B !important;
        border-color: #FF4B4B !important;
        color: #ffffff !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(255, 75, 75, 0.4) !important;
    }
    div[data-testid="stColumn"] div.stButton > button:disabled {
        background: rgba(255, 255, 255, 0.04) !important;
        border-color: rgba(255, 255, 255, 0.06) !important;
        opacity: 0.25 !important;
        cursor: not-allowed !important;
    }
</style>
""", unsafe_allow_html=True)

# --- ESTADO DA SESSÃO (SESSION STATE) ---
if "user_ranking" not in st.session_state:
    st.session_state.user_ranking = list(FILMES_DREAMWORKS)

def move_up(index):
    if index > 0:
        lst = st.session_state.user_ranking
        lst[index - 1], lst[index] = lst[index], lst[index - 1]

def move_down(index):
    lst = st.session_state.user_ranking
    if index < len(lst) - 1:
        lst[index + 1], lst[index] = lst[index], lst[index + 1]

# --- CABEÇALHO ---
st.markdown('<p class="main-title">🎬 DreamMatch: Recomendador DreamWorks</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Ordene seus filmes favoritos e descubra com qual perfil da DreamWorks você tem maior sintonia cinematográfica!</p>', unsafe_allow_html=True)

# Layout em duas colunas principais
col_left, col_right = st.columns([1, 1], gap="large")

# =========================================================================
# COLUNA ESQUERDA: DEFINIÇÃO DE PREFERÊNCIAS DO USUÁRIO
# =========================================================================
with col_left:
    st.subheader("1. Seu Top 10 de Preferências")
    st.markdown("Use as setas ⬆️ / ⬇️ para posicionar os filmes do seu **favorito (1º)** até o **menos preferido (10º)**.")
    st.write("")

    # Lista interativa com botões de subir e descer
    for idx, filme in enumerate(st.session_state.user_ranking):
        meta = FILMES_METADATA.get(filme, {"ano": "", "genero": ""})
        row_c1, row_c2, row_c3 = st.columns([0.8, 6.4, 2.0], vertical_alignment="center")
        
        with row_c1:
            st.markdown(f"<span style='color: #FF8533; font-weight: 700; font-size: 1.05rem;'>#{idx + 1}</span>", unsafe_allow_html=True)
        
        with row_c2:
            st.markdown(f"**{filme}** ({meta['ano']})  \n<small style='color: #888;'>{meta['genero']}</small>", unsafe_allow_html=True)
            
        with row_c3:
            b_up, b_down = st.columns(2, gap="small")
            with b_up:
                if st.button("▲", key=f"up_{idx}", disabled=(idx == 0), use_container_width=True, help="Subir filme"):
                    move_up(idx)
                    st.rerun()
            with b_down:
                if st.button("▼", key=f"down_{idx}", disabled=(idx == len(st.session_state.user_ranking) - 1), use_container_width=True, help="Descer filme"):
                    move_down(idx)
                    st.rerun()

# =========================================================================
# COLUNA DIREITA: RESULTADOS E COMPARAÇÃO
# =========================================================================
with col_right:
    st.subheader("2. Resultados da Análise de Similaridade")

    # Executa a comparação via Dividir e Conquistar
    ranking_perfis = rankear_perfis(st.session_state.user_ranking, PERFIS_FICTICIOS)
    melhor = ranking_perfis[0]

    # Card de Destaque para o Perfil Vencedor
    st.markdown(f"""
    <div class="winner-card">
        <h3 style="margin-top:0; color:#FF4B4B;">✨ Perfil Mais Compatível! ✨</h3>
        <h1 style="font-size: 2.8rem; margin: 10px 0;">{melhor['avatar']}</h1>
        <h2 style="margin: 0;">{melhor['nome']}</h2>
        <p style="color: #bbb; font-style: italic; margin-top: 5px;">"{melhor['descricao']}"</p>
        <div style="margin: 15px 0;">
            <span style="font-size: 2.2rem; font-weight: 800; color: #00CC66;">{melhor['similaridade']}%</span>
            <span style="color: #aaa; margin-left: 8px;">de compatibilidade</span>
        </div>
        <p style="margin-bottom: 0;">
            Apenas <b>{melhor['inversoes']}</b> inversão(ões) de um máximo de 45 pares possíveis.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Gráfico / Lista de todos os perfis
    st.markdown("#### Ranking de Similaridade com Todos os Perfis")
    
    df_ranking = pd.DataFrame([
        {
            "Perfil": f"{p['avatar']} {p['nome']}",
            "Similaridade": p["similaridade"],
            "Inversões": f"{p['inversoes']} / 45"
        }
        for p in ranking_perfis
    ])
    
    st.dataframe(
        df_ranking,
        column_config={
            "Similaridade": st.column_config.ProgressColumn(
                "Similaridade",
                help="Percentual de concordância relativa entre pares de filmes",
                format="%.1f%%",
                min_value=0,
                max_value=100
            )
        },
        hide_index=True,
        use_container_width=True
    )

    # Detalhes e Inversões
    with st.expander("🔍 Ver Detalhes das Comparações e Pares Discordantes"):
        tab_titles = [f"{p['avatar']} {p['nome'].split()[0]}" for p in ranking_perfis]
        tabs = st.tabs(tab_titles)
        
        for tab, perfil in zip(tabs, ranking_perfis):
            with tab:
                st.markdown(f"**Perfil:** {perfil['nome']}")
                st.markdown(f"**Descrição:** {perfil['descricao']}")
                st.markdown(f"**Total de Inversões:** `{perfil['inversoes']}` | **Similaridade:** `{perfil['similaridade']}%`")
                
                st.markdown("**Top 3 Filmes deste perfil:**")
                st.markdown(f"1. 🥇 {perfil['ranking'][0]}  \n2. 🥈 {perfil['ranking'][1]}  \n3. 🥉 {perfil['ranking'][2]}")
                
                if perfil["inversoes"] == 0:
                    st.success("🎉 Nenhuma inversão! A ordem de vocês é 100% idêntica.")
                else:
                    st.markdown(f"**Pares Discordantes (Inversões encontradas: {len(perfil['pares_invertidos'])}):**")
                    st.caption("Filmes que este perfil prefere antes, mas que você colocou depois:")
                    pares_txt = [f"• **{a}** antes de **{b}**" for a, b in perfil["pares_invertidos"][:6]]
                    if len(perfil["pares_invertidos"]) > 6:
                        pares_txt.append(f"*(e mais {len(perfil['pares_invertidos']) - 6} pares...)*")
                    st.markdown("\n".join(pares_txt))


