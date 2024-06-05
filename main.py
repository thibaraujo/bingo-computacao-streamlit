import streamlit as st
import numpy as np
import random

animais = [
    "Cachorro", "Gato", "Elefante", "Leão", "Tigre", "Urso", "Zebra", "Girafa",
    "Rinoceronte", "Hipopótamo", "Cavalo", "Cobra", "Jacaré", "Águia", "Papagaio",
    "Macaco", "Panda", "Canguru", "Lobo", "Rato", "Coelho", "Raposa", "Tartaruga", "Foca", "Pinguim"
]

def gerar_bingo():
    random.shuffle(animais)
    selecionados = animais[:24]
    tabela = np.array(selecionados[:12] + ["Bingo"] + selecionados[12:]).reshape(5, 5).tolist()
    return tabela

if 'tabela' not in st.session_state:
    st.session_state['tabela'] = gerar_bingo()

if 'marcados' not in st.session_state:
    st.session_state['marcados'] = [[False]*5 for _ in range(5)]

def renderizar_bingo(tabela, marcados):
    table_html = "<div style='overflow-x: auto; white-space: nowrap;'>"
    table_html += "<table>"
    for i in range(5):
        table_html += "<tr>"
        for j in range(5):
            cell_label = tabela[i][j]
            button_key = f'{i}-{j}'
            if st.button(cell_label, key=button_key, help=f"{i}-{j}"):
                marcados[i][j] = not marcados[i][j]
            cell_style = "background-color: lightgreen;" if marcados[i][j] else ""
            table_html += f"<td style='{cell_style}'>{cell_label}</td>"
        table_html += "</tr>"
    table_html += "</table>"
    table_html += "</div>"

    st.write(table_html, unsafe_allow_html=True)

st.title('Bingo da Computação')
st.write('Clique nas palavras para marcar/desmarcar.')

renderizar_bingo(st.session_state['tabela'], st.session_state['marcados'])
