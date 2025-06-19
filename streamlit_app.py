import streamlit as st

# Configuração da página
st.set_page_config(page_title="Portfólio Kipper", layout="wide")

# Foto principal
st.image(
    "https://ccbj.org.br/wp-content/uploads/2024/05/03.05.2024-Montilla-Coca-Cola-flavia-almeida-8-1024x683.jpg",
    use_column_width=True,
    caption="Kipper em performance — Foto: Flavia Almeida / CCBJ"
)

# Cabeçalho
st.title("🎭 Portfólio de Kipper")
st.markdown("Ator. Criador. Intérprete. Esta é a trajetória artística de Kipper contada através de sua obra.")

# Trajetória
st.header("🌟 Trajetória")
st.write("""
Kipper é um artista cearense que iniciou sua jornada nos espaços públicos e nas linguagens experimentais. 
Seus trabalhos cruzam teatro, dança, performance e audiovisual, abordando temas sociais, identitários e afetivos com força poética.
""")

# Galeria de fotos
st.header("🖼️ Galeria de Fotos")
imagens = [
    "https://link1-da-galeria.jpg",
    "https://link2-da-galeria.jpg"
]
for img in imagens:
    st.image(img, use_column_width=True)

# Vídeos do YouTube
st.header("🎥 Obras em Vídeo")
st.video("https://www.youtube.com/watch?v=video_id1")
st.video("https://www.youtube.com/watch?v=video_id2")

# Contato
st.header("📬 Contato")
with st.form("form_contato"):
    nome = st.text_input("Seu nome")
    email = st.text_input("Seu e-mail")
    mensagem = st.text_area("Mensagem para Kipper")
    enviar = st.form_submit_button("Enviar")
    if enviar:
        st.success("Mensagem enviada com sucesso! Obrigado por entrar em contato.")

st.markdown("---")
st.caption("© Kipper • Portfólio criado com Streamlit")
