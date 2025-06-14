import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Painel de Controle Orion", page_icon="💡", layout="centered")

# --- FUNÇÃO PARA GERAR OS PROMPTS ---
def gerar_prompts(pilar, prompt_extra):
    """Gera os prompts de texto e imagem com base na seleção do usuário."""
    
    # Prompt base para o texto
    prompt_texto = f"""Aja como um Diretor de Criação para a empresa de segurança eletrônica 'Orion System'.
Sua tarefa é criar um conceito completo para um post de rede social (Instagram).

**Pilar de Conteúdo Principal:** {pilar}
**Instrução Adicional do Usuário:** {prompt_extra if prompt_extra else "Nenhuma."}
**Marca:** Orion System
**Cores da Marca:** Azul escuro, Laranja e Branco.

**Por favor, gere o seguinte:**
1.  **Título Curto e Impactante:** Um título para ser colocado sobre a imagem (máximo de 10 palavras).
2.  **Legenda para Rede Social:** Uma legenda com 2 ou 3 parágrafos curtos, terminando com uma chamada para ação e incluindo hashtags relevantes para o negócio (#SegurancaEletronica, #CasaSegura, #OrionSystem, etc.).
"""

    # Prompt base para a imagem
    prompt_imagem = f"""Crie uma imagem fotorealista, cinematográfica e de alta qualidade no formato retrato (proporção 10:16).
O conceito principal é "{pilar}".
A imagem deve ser para a empresa de segurança 'Orion System' e evocar sentimentos de segurança, tecnologia e tranquilidade.
Instrução adicional: "{prompt_extra if prompt_extra else "Focar no sentimento do pilar principal."}"
Use uma paleta de cores que remeta a azul escuro, laranja e branco, mas de forma natural na cena.
Não inclua nenhum texto ou logo na imagem.
"""
    
    return prompt_texto, prompt_imagem

# --- INTERFACE DO USUÁRIO ---
st.title("💡 Painel de Controle Orion")
st.write("Gere os prompts perfeitos para criar seus posts em ferramentas de IA gratuitas.")

try:
    st.sidebar.image("orion-logo.png", width=200)
except FileNotFoundError:
    st.sidebar.error("Logo não encontrada!")

st.sidebar.header("Configurações do Post")
pilar_conteudo = st.sidebar.selectbox(
    "Escolha o Pilar de Conteúdo",
    ("Selecione...", "Tranquilidade e Paz", "Família e Proteção", "Tecnologia e Controle", "Liberdade e Viagem")
)
prompt_adicional = st.sidebar.text_area("Instrução Adicional:", placeholder="Ex: Focar em câmeras com visão noturna...")

gerar_btn = st.sidebar.button("Gerar Prompts ✍️", type="primary")

# --- LÓGICA PRINCIPAL ---
if gerar_btn:
    if pilar_conteudo == "Selecione...":
        st.error("Por favor, selecione um pilar de conteúdo.")
    else:
        with st.spinner("Gerando prompts inteligentes..."):
            prompt_final_texto, prompt_final_imagem = gerar_prompts(pilar_conteudo, prompt_adicional)
            
            st.balloons()
            st.header("✅ Prompts Gerados com Sucesso!")
            
            st.subheader("1. Prompt para o Texto")
            st.info("Copie este prompt e cole no Gemini (gemini.google.com) ou ChatGPT gratuito.")
            st.text_area("Prompt de Texto", value=prompt_final_texto, height=250)
            
            st.subheader("2. Prompt para a Imagem")
            st.warning("Copie este prompt e cole no Microsoft Copilot Designer (bing.com/create).")
            st.text_area("Prompt de Imagem", value=prompt_final_imagem, height=200)import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Painel de Controle Orion", page_icon="💡", layout="centered")

# --- FUNÇÃO PARA GERAR OS PROMPTS ---
def gerar_prompts(pilar, prompt_extra):
    """Gera os prompts de texto e imagem com base na seleção do usuário."""
    
    # Prompt base para o texto
    prompt_texto = f"""Aja como um Diretor de Criação para a empresa de segurança eletrônica 'Orion System'.
Sua tarefa é criar um conceito completo para um post de rede social (Instagram).

**Pilar de Conteúdo Principal:** {pilar}
**Instrução Adicional do Usuário:** {prompt_extra if prompt_extra else "Nenhuma."}
**Marca:** Orion System
**Cores da Marca:** Azul escuro, Laranja e Branco.

**Por favor, gere o seguinte:**
1.  **Título Curto e Impactante:** Um título para ser colocado sobre a imagem (máximo de 10 palavras).
2.  **Legenda para Rede Social:** Uma legenda com 2 ou 3 parágrafos curtos, terminando com uma chamada para ação e incluindo hashtags relevantes para o negócio (#SegurancaEletronica, #CasaSegura, #OrionSystem, etc.).
"""

    # Prompt base para a imagem
    prompt_imagem = f"""Crie uma imagem fotorealista, cinematográfica e de alta qualidade no formato retrato (proporção 10:16).
O conceito principal é "{pilar}".
A imagem deve ser para a empresa de segurança 'Orion System' e evocar sentimentos de segurança, tecnologia e tranquilidade.
Instrução adicional: "{prompt_extra if prompt_extra else "Focar no sentimento do pilar principal."}"
Use uma paleta de cores que remeta a azul escuro, laranja e branco, mas de forma natural na cena.
Não inclua nenhum texto ou logo na imagem.
"""
    
    return prompt_texto, prompt_imagem

# --- INTERFACE DO USUÁRIO ---
st.title("💡 Painel de Controle Orion")
st.write("Gere os prompts perfeitos para criar seus posts em ferramentas de IA gratuitas.")

try:
    st.sidebar.image("orion-logo.png", width=200)
except FileNotFoundError:
    st.sidebar.error("Logo não encontrada!")

st.sidebar.header("Configurações do Post")
pilar_conteudo = st.sidebar.selectbox(
    "Escolha o Pilar de Conteúdo",
    ("Selecione...", "Tranquilidade e Paz", "Família e Proteção", "Tecnologia e Controle", "Liberdade e Viagem")
)
prompt_adicional = st.sidebar.text_area("Instrução Adicional:", placeholder="Ex: Focar em câmeras com visão noturna...")

gerar_btn = st.sidebar.button("Gerar Prompts ✍️", type="primary")

# --- LÓGICA PRINCIPAL ---
if gerar_btn:
    if pilar_conteudo == "Selecione...":
        st.error("Por favor, selecione um pilar de conteúdo.")
    else:
        with st.spinner("Gerando prompts inteligentes..."):
            prompt_final_texto, prompt_final_imagem = gerar_prompts(pilar_conteudo, prompt_adicional)
            
            st.balloons()
            st.header("✅ Prompts Gerados com Sucesso!")
            
            st.subheader("1. Prompt para o Texto")
            st.info("Copie este prompt e cole no Gemini (gemini.google.com) ou ChatGPT gratuito.")
            st.text_area("Prompt de Texto", value=prompt_final_texto, height=250)
            
            st.subheader("2. Prompt para a Imagem")
            st.warning("Copie este prompt e cole no Microsoft Copilot Designer (bing.com/create).")
            st.text_area("Prompt de Imagem", value=prompt_final_imagem, height=200)