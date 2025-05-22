import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Projetos com Notebooks", layout="wide")
st.title("📘 Projeto: Visualização de Notebooks")
st.markdown("---")

tabs = st.tabs(["📊 Limpeza de Dados", "🧠 Funções Python", "📂 Operações com Listas"])

# --- Limpeza de Dados ---
with tabs[0]:
    st.subheader("📊 Limpeza e Preparação de Dados")
    st.markdown("Demonstrações de como importar, limpar e preparar dados em um dataset.")

    with st.expander("📥 Importação de bibliotecas"):
        st.code("import pandas as pd\nimport numpy as np", language="python")

    with st.expander("📄 Leitura e visualização inicial"):
        st.code('df = pd.read_csv("DADOS_ALUNOS.csv", sep=";")\ndf.head()', language="python")

    with st.expander("🔍 Verificação e tratamento de dados ausentes"):
        st.code('df.isnull().sum()\ndf["Nota"] = df["Nota"].fillna(0)', language="python")

    with st.expander("🧹 Remoção de duplicatas e renomeação"):
        st.code('df = df.drop_duplicates()\ndf = df.rename(columns={"Nota": "Nota_Final"})\ndf.head()', language="python")

# --- Funções ---
with tabs[1]:
    st.subheader("🧠 Funções em Python")
    st.markdown("Exemplos de criação e uso de funções, incluindo parâmetros padrão e retornos múltiplos.")

    with st.expander("🙋‍♀️ Saudação personalizada"):
        st.code("""
def saudacao(nome):
    return f"Olá, {nome}!"
""", language="python")

    with st.expander("📐 Função com parâmetro padrão"):
        st.code("""
def potencia(base, expoente=2):
    return base ** expoente

potencia(3)      # 3² = 9
potencia(3, 3)   # 3³ = 27
""", language="python")

    with st.expander("🔁 Retorno múltiplo"):
        st.code("""
def operacoes(a, b):
    soma = a + b
    sub = a - b
    return soma, sub

s, sub = operacoes(10, 5)
print(f"Soma: {s}, Subtração: {sub}")
""", language="python")

    with st.expander("💬 Repetição com argumentos nomeados"):
        st.code("""
def mensagem(texto, vezes=1):
    for _ in range(vezes):
        print(texto)

mensagem("Estudando funções", 3)
""", language="python")

# --- Listas e Operações ---
with tabs[2]:
    st.subheader("📂 Operações com Listas (2CDD02)")
    st.markdown("Códigos para manipulação de listas e estruturas em Python.")

    with st.expander("➕ Soma e média"):
        st.code("""
lista = [1, 2, 3, 4, 5]
soma = sum(lista)
media = soma / len(lista)
print(f"Soma: {soma}, Média: {media}")
""", language="python")

    with st.expander("📐 Quadrados com list comprehension"):
        st.code("""
quadrados = [x**2 for x in lista]
print("Quadrados:", quadrados)
""", language="python")

    with st.expander("📍 Enumerando elementos"):
        st.code("""
for i, valor in enumerate(lista):
    print(f"Índice: {i}, Valor: {valor}")
""", language="python")

    with st.expander("📏 Fatiamento e modificação"):
        st.code("""
print(lista[1:4])  # do segundo ao quarto elemento

lista.append(6)
lista.remove(2)
print(lista)
""", language="python")
