import streamlit as st
import google.generativeai as genai
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# --- CONFIGURAÇÃO DA PÁGINA E API ---
st.set_page_config(page_title="Orion Content Factory", page_icon="🤖", layout="centered")

# Acessa a chave da API guardada nos segredos do Streamlit
# Acessa o segredo como um dicionário, usando o nome exato da chave como uma string
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except (KeyError, AttributeError):
    st.error("Chave da API do Gemini não encontrada. Verifique se seu arquivo .streamlit/secrets.toml existe e está correto.")
    st.stop()

# --- FUNÇÕES AUXILIARES ---
def gerar_conteudo_ia(pilar, prompt_extra):
    """Gera o conceito de texto e descrição da imagem usando a IA do Gemini."""
    modelo_texto = genai.GenerativeModel('gemini-1.5-pro-latest')
    prompt_template = f"""
    Aja como um Diretor de Criação para a empresa de segurança 'Orion System'.
    Sua tarefa é criar um conceito para um post de Instagram (1080x1350).
    Pilar de Conteúdo: {pilar}
    Instrução Adicional: {prompt_extra if prompt_extra else "Nenhuma."}
    Marca: Orion System. Cores: Azul escuro, Laranja, Branco.
    Responda APENAS com o texto no formato abaixo, sem explicações:
    TITULO: [Crie um título curto e impactante para a imagem. Máximo 10 palavras.]
    LEGENDA: [Crie uma legenda para a rede social com 2 parágrafos, hashtags e CTA.]
    IMAGEM_DESC: [Descreva uma imagem fotorealista detalhada para o post. Inclua cena, iluminação e emoções.]
    """
    try:
        resposta = modelo_texto.generate_content(prompt_template)
        return resposta.text
    except Exception as e:
        st.error(f"Erro ao chamar a API do Gemini: {e}")
        return None

def gerar_imagem_com_pil(descricao, texto_titulo):
    """Gera uma imagem final com texto e logo usando Pillow."""
    try:
        img_base = Image.new('RGB', (1080, 1350), color = '#003366') # Azul escuro da Orion
        logo_path="orion-logo.png"
        logo = Image.open(logo_path).convert("RGBA")
        
        logo_largura = int(img_base.width / 5)
        ratio = logo_largura / float(logo.size[0])
        logo_altura = int(float(logo.size[1]) * float(ratio))
        logo = logo.resize((logo_largura, logo_altura), Image.LANCZOS)
        img_base.paste(logo, (40, 40), logo)

        draw = ImageDraw.Draw(img_base)
        try:
            fonte_titulo = ImageFont.truetype("Montserrat-Bold.ttf", size=90)
            fonte_desc = ImageFont.truetype("Montserrat-Regular.ttf", size=30)
        except IOError:
            st.warning("Fonte 'Montserrat' não encontrada. Usando fonte padrão.")
            fonte_titulo = ImageFont.load_default(size=90)
            fonte_desc = ImageFont.load_default(size=30)
        
        caixa_texto = draw.textbbox((0, 0), texto_titulo, font=fonte_titulo, anchor="lt")
        largura_texto = caixa_texto[2] - caixa_texto[0]
        altura_texto = caixa_texto[3] - caixa_texto[1]
        pos_x = (1080 - largura_texto) / 2
        pos_y = (1350 - altura_texto) / 2
        draw.text((pos_x, pos_y), texto_titulo, font=fonte_titulo, fill="white", stroke_width=3, stroke_fill="#002244")

        draw.text((40, 1200), f"Conceito Visual:\n{descricao[:100]}...", font=fonte_desc, fill="#DDDDDD")

        buffer = BytesIO()
        img_base.save(buffer, format="PNG")
        buffer.seek(0)
        return buffer
    except Exception as e:
        st.error(f"Erro ao montar imagem com Pillow: {e}")
        return None

# --- INTERFACE DO USUÁRIO ---
st.title("🏭 Orion Content Factory")
try:
    st.sidebar.image("orion-logo.png", width=200)
except FileNotFoundError:
    st.sidebar.error("Logo não encontrada! Verifique se 'orion-logo.png' está na pasta.")

st.sidebar.header("Configurações do Post")
pilar_conteudo = st.sidebar.selectbox("Escolha o Pilar", ("Selecione...", "Tranquilidade e Paz", "Família e Proteção", "Tecnologia e Controle", "Liberdade e Viagem"))
prompt_adicional = st.sidebar.text_area("Instrução Adicional:", placeholder="Ex: Falar sobre o Dia dos Pais...")
gerar_btn = st.sidebar.button("Gerar Post ✨", type="primary")

# --- LÓGICA PRINCIPAL ---
if gerar_btn:
    if pilar_conteudo == "Selecione...":
        st.error("Por favor, selecione um pilar de conteúdo.")
    else:
        with st.spinner("Gerando conceito e texto... 🧠"):
            conteudo_gerado = gerar_conteudo_ia(pilar_conteudo, prompt_adicional)
        
        if conteudo_gerado:
            try:
                titulo = conteudo_gerado.split("TITULO:")[1].split("LEGENDA:")[0].strip()
                legenda = conteudo_gerado.split("LEGENDA:")[1].split("IMAGEM_DESC:")[0].strip()
                img_desc = conteudo_gerado.split("IMAGEM_DESC:")[1].strip()
            except IndexError:
                st.error("A IA não retornou o formato esperado. O resultado bruto foi:")
                st.code(conteudo_gerado)
                st.stop()
            
            with st.spinner("Desenhando a imagem final... 🎨"):
                imagem_final = gerar_imagem_com_pil(img_desc, titulo)
            
            st.balloons()
            st.header("✅ Post Gerado com Sucesso!")
            if imagem_final:
                st.image(imagem_final, caption="Sua imagem final está pronta.")
                st.download_button("Baixar Imagem", data=imagem_final, file_name="post_orion.png", mime="image/png")
            st.subheader("Textos Prontos para Copiar:")
            st.text_input("Título:", value=titulo)
            st.text_area("Legenda:", value=legenda, height=250)