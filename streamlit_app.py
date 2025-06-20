import streamlit as st

st.set_page_config(layout="wide", page_title="Menu Colapsável", page_icon="📁")

st.sidebar.title("📋 Menu")

# Menu colapsável com expander
with st.sidebar.expander("📦 Produtos"):
    pagina = st.radio("Selecione a ação:", [
        "Dashboard",
        "Criar Produto",
        "Consultar Produto",
        "Editar Produto",
        "Excluir Produto"
    ])

st.title(f"🛠️ {pagina}")

# Banco simulado
produtos = ["Notebook Gamer", "Camisa Social", "Chá Verde"]

# Seções de conteúdo
if pagina == "Dashboard":
    st.info("Painel geral com visão rápida do sistema.")

elif pagina == "Criar Produto":
    with st.form("criar_produto"):
        nome = st.text_input("Nome do Produto")
        preco = st.number_input("Preço (R$)", min_value=0.0, format="%.2f")
        estoque = st.number_input("Estoque", min_value=0)
        publicado = st.checkbox("Publicado?")
        salvar = st.form_submit_button("Salvar")
        if salvar:
            st.success(f"Produto '{nome}' criado!")

elif pagina == "Consultar Produto":
    produto = st.selectbox("Selecione um produto", produtos)
    st.write(f"**Produto:** {produto}")
    st.write("Preço: R$149,90\nEstoque: 27 unidades\nPublicado: Sim")

elif pagina == "Editar Produto":
    produto = st.selectbox("Editar produto", produtos)
    with st.form("editar_produto"):
        nome = st.text_input("Nome do Produto", value=produto)
        preco = st.number_input("Preço (R$)", value=99.90)
        estoque = st.slider("Estoque", 0, 100, 25)
        publicado = st.radio("Publicado?", ["Sim", "Não"])
        atualizar = st.form_submit_button("Atualizar")
        if atualizar:
            st.success(f"'{nome}' atualizado!")

elif pagina == "Excluir Produto":
    produto = st.selectbox("Produto a excluir", produtos)
    confirmar = st.button("Excluir")
    if confirmar:
        st.error(f"Produto '{produto}' foi excluído.")

st.markdown("---")
st.caption("🔧 Menu com expander em Streamlit • Estilo colapsável simples")
