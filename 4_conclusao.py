import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet
from datetime import timedelta
import base64
import numpy as np


def background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    main_bg = "Base de Dados\sample_3.png"

    # background(main_bg)

    st.subheader(':red[Conclusão]')

    st.subheader(':gray[Resultados e Eficiência do Prophet na Previsão]', divider='red')

    st.markdown('''
                Dos resultados obtidos, observamos um WMAPE de aproximadamente 7% \\ao analisarmos os últimos 10 anos, havendo variação conforme aumento ou diminuição do tempo analisado no modelo, o que indica que o mesmo está apresentando uma precisão de aproximadamente 93% nas previsões realizadas. Esse valor é considerado satisfatório, pois está relativamente baixo, sugerindo que o modelo é eficaz em capturar a maior parte da variabilidade nos dados e em prever com precisão o preço do petróleo. \n 

                Em suma, os resultados obtidos demonstram a robustez e a precisão do Prophet na tarefa de prever o preço do petróleo, considerando as características dos dados temporais e sazonais.
                ''')
    
    st.subheader(':gray[Melhorias futuras]', divider='red')

    st.markdown('''
                Apesar de o modelo Prophet ter apresentado resultados satisfatórios, ainda há espaço para melhorias e otimizações futuras. Algumas sugestões de aprimoramento incluem: \n

                :one: **Ajuste de Hiperparâmetros**: O Prophet possui diversos hiperparâmetros que podem ser ajustados para melhorar a precisão das previsões. Realizar uma busca sistemática de hiperparâmetros pode ajudar a encontrar a combinação ideal para o conjunto de dados analisado. \n

                ''')

main()  