import streamlit as st

# Configuração da página
st.set_page_config(layout="wide", page_title="Painel Admin", page_icon="🛠️")

# Banco de dados simulado (lista estática)
produtos = ["Fone de ouvido", "Camiseta Azul", "Café Especial"]

# Menu lateral nativo
menu = st.sidebar.radio(
    "📋 Menu",
    ("Dashboard", "Criar Produto", "Consultar Produto", "Editar Produto", "Excluir Produto")
)

st.title(f"🛠️ {menu}")

# CRUD
if menu == "Dashboard":
    st.info("Bem-vindo! Use o menu à esquerda para gerenciar os produtos.")

elif menu == "Criar Produto":
    st.subheader("📦 Criar Novo Produto")
    with st.form("form_create"):
        nome = st.text_input("Nome do Produto")
        preco = st.number_input("Preço (R$)", min_value=0.0, format="%.2f")
        estoque = st.number_input("Estoque", min_value=0, step=1)
        categoria = st.selectbox("Categoria", ["Eletrônicos", "Roupas", "Alimentos", "Outro"])
        publicado = st.checkbox("Publicado?", value=True)
        salvar = st.form_submit_button("Salvar")
        if salvar:
            st.success(f"Produto '{nome}' cadastrado com sucesso!")

elif menu == "Consultar Produto":
    st.subheader("🔍 Consulta de Produtos")
    produto = st.selectbox("Escolha um produto", produtos)
    st.write(f"**Produto:** {produto}")
    st.write("Preço: R$99,00\nEstoque: 42 unidades\nCategoria: Eletrônicos\nPublicado: Sim")

elif menu == "Editar Produto":
    st.subheader("📝 Editar Produto")
    produto = st.selectbox("Selecione um produto", produtos)
    with st.form("form_edit"):
        nome = st.text_input("Nome do Produto", value=produto)
        preco = st.number_input("Preço (R$)", value=89.90)
        estoque = st.slider("Estoque", 0, 100, 42)
        publicado = st.radio("Publicado?", ["Sim", "Não"])
        atualizar = st.form_submit_button("Atualizar")
        if atualizar:
            st.success(f"Produto '{nome}' atualizado com sucesso!")

elif menu == "Excluir Produto":
    st.subheader("❌ Remover Produto")
    produto = st.selectbox("Escolha um produto para excluir", produtos)
    excluir = st.button("Excluir")
    if excluir:
        st.error(f"Produto '{produto}' removido com sucesso!")

st.markdown("---")
st.caption("🎛️ Painel em Streamlit • Simples e direto, sem bibliotecas externas")
