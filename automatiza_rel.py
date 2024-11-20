import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt



username = 'Vini'

# Título da aplicação
st.title("Análise de Dados - EDA")
st.write(f"Bem-vindo, {username}!")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Envie o arquivo CSV (processo_atualizado.csv)", type=["csv"])

if uploaded_file:
    # Carregar o DataFrame
    df = pd.read_csv(uploaded_file)
    st.write("Visualizando os Dados:")
    st.write(df.head())

    # Gráfico de Resolução
    st.subheader("Distribuição por Resolução")
    fig, ax = plt.subplots(figsize=(8, 6))
    df['Resolução'].value_counts(normalize=True).plot(
        kind='barh',
        ax=ax,
        color='skyblue'
    )
    ax.set_xlabel('Porcentagem')
    ax.set_ylabel('Resolução')
    for bar in ax.patches:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2%}',
                va='center', ha='left', fontsize=10)
    st.pyplot(fig)

    # Status por Método de Contato
    st.subheader("Desempenho por Método de Contato")
    status_contato = pd.crosstab(df['Método de Contato'], df['Status'])
    status_contato['Desempenho'] = (status_contato['Concluído'] / 
                                   (status_contato['Concluído'] + status_contato['Aberto'])).round(2)

    st.write("Tabela de desempenho:")
    st.dataframe(status_contato)

    # Gráfico de desempenho por método de contato
    st.subheader("Métodos com Desempenho Acima da Média")
    metodos_acima = status_contato.loc[status_contato['Desempenho'] > status_contato['Desempenho'].mean()]
    fig, ax = plt.subplots()
    metodos_acima['Desempenho'].plot(kind='bar', ax=ax, color='green')
    ax.set_ylabel('Desempenho')
    ax.set_xlabel('Método de Contato')
    plt.xticks(rotation=45)
    st.pyplot(fig)
