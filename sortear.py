import os
import random
import streamlit as st

# Caminho para a pasta com os vídeos
video_folder = 'midia'

# Função para listar os arquivos MP4 na pasta
def list_videos(folder):
    return [f for f in os.listdir(folder) if f.endswith('.mp4')]

# Função para sortear um vídeo que ainda não foi sorteado
def sorteia_video(videos, sorteados):
    disponiveis = list(set(videos) - set(sorteados))
    if not disponiveis:
        return None
    return random.choice(disponiveis)


if 'videos' not in st.session_state:
    st.session_state.videos = list_videos(video_folder)
    st.session_state.sorteados = []

st.title('Sorteio de Vídeos')

if st.button('Sortear'):
    video = sorteia_video(st.session_state.videos, st.session_state.sorteados)
    if video:
        st.session_state.sorteados.append(video)
        video_path = os.path.join(video_folder, video)

        cols = st.columns([1, 2, 1])
        with cols[1]:
            st.video(video_path, format="video/mp4", start_time=0)
    else:
        st.write("Todos os vídeos foram sorteados.")


print("Histórico de vídeos sorteados:")
print(st.session_state.sorteados)