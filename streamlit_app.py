import streamlit as st

# Configuração da página
st.set_page_config(page_title="Portfólio Kipper", layout="wide")

# Cabeçalho
st.title("🎭 Portfólio de Kipper")
st.markdown("Ator. Criador. Intérprete. Esta é a trajetória artística de Kipper contada através de sua obra.")

# Seção: Trajetória
st.header("🌟 Trajetória")
st.write("""
Kipper iniciou sua carreira nas artes cênicas ainda jovem, explorando o teatro de rua e a performance urbana. 
Ao longo dos anos, seu trabalho evoluiu para incluir vídeo arte, fotografia conceitual e colaborações interdisciplinares.
""")

# Seção: Fotos do trabalho
st.header("🖼️ Galeria de Fotos")
imagens = [
    "https://link-de-alguma-foto.jpg",
    "https://outra-foto.jpg"
]
for img in imagens:
    st.image(img, use_column_width=True)

# Seção: Vídeos
st.header("🎥 Obras em Vídeo")
st.video("https://www.youtube.com/watch?v=link_do_video1")
st.video("https://www.youtube.com/watch?v=link_do_video2")

# Seção: Contato
st.header("📬 Contato")
with st.form("form_contato"):
    nome = st.text_input("Seu nome")
    email = st.text_input("Seu e-mail")
    mensagem = st.text_area("Mensagem para Kipper")
    enviar = st.form_submit_button("Enviar")
    if enviar:
        st.success("Mensagem enviada com sucesso! Obrigado por entrar em contato.")

st.markdown("---")
st.caption("©
