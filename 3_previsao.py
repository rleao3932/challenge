import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet
from datetime import timedelta, datetime
import base64, os
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

def atualizar_base_dados():
    try:
        dados = pd.read_html('http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view', decimal=',', thousands='.')
        dados[2] = dados[2].loc[1:]
        dados = pd.DataFrame(dados[2])
        dados[0] = pd.to_datetime(dados[0], format='%d/%m/%Y')
        dados.rename(columns={0: 'data', 1: 'preco'}, inplace=True)
        dados['preco'] = dados['preco'].str.replace('.', ',')
        dados.to_csv('Base de dados\\dados.csv', sep=';', encoding='utf-8')
    except:
        return False
    else:
        return True

def main():

    # background(main_bg)

    st.subheader(':red[Análise de Preço do Petróleo Brent 🛢️]', divider='red')
    arquivo = 'Base de dados\\dados.csv'
    df = pd.read_csv(arquivo, sep=';')
    timestamp_modificacao = os.path.getmtime(arquivo)
    data_modificacao = datetime.fromtimestamp(timestamp_modificacao).date()
    hoje = datetime.now().date()
    
    col1, col2 = st.columns((1,1))
    with col1: 
        years = st.number_input("Quantos anos quer usar de base? Padrão 10 anos. Mínimo 5 anos.", min_value=5, max_value=50, value=10)
        if st.button("Atualizar base de dados"):
            if atualizar_base_dados():
                st.write("A base de dados está atualizada.")
                st.rerun()
            else:
                st.write("Erro ao atualizar base, utilizando a mais recente disponível no diretório do projeto.")
        if data_modificacao == hoje:
            st.write("A base de dados está atualizada.")
        

    df = df[['data', 'preco']]
    df = df.rename(columns={'data': 'Data', 'preco': 'Preço Petróleo Brent'})
    df['Data'] = pd.to_datetime(df['Data'])

    df_prophet = df[(df['Data'] >= df['Data'].max() - timedelta(days=years * 365))]
    df_prophet.rename(columns={'Data': 'ds', 'Preço Petróleo Brent': 'y'}, inplace=True)
    df_prophet['y'] = df_prophet['y'].str.replace(',', '.').astype(float)
    df_prophet = df_prophet.set_index('ds')
    idx = pd.date_range(start=df_prophet.index.min(), end=df_prophet.index.max())
    df_prophet = df_prophet.reindex(idx)
    df_prophet['y'] = df_prophet['y'].ffill()
    df_prophet.isnull().sum()
    df_prophet = df_prophet.reset_index()
    df_prophet.rename(columns={'index': 'ds'}, inplace=True)

    model = Prophet(daily_seasonality=True)
    model.fit(df_prophet)

    with col2:
        days = st.number_input("Quantos dias para prever?", min_value=1, max_value=365, value=30)
    future = model.make_future_dataframe(periods=days)

    st.divider()

    col3, col4 = st.columns(2)

    with col3:
        st.write(f'### Projeção de preço - {days} dias')
        forecast = model.predict(future)
        forecast2 = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].sort_values(by='ds', ascending=False)
        # Calcula WMAPE
        forecast_real = df_prophet[df_prophet['ds'].isin(forecast['ds'])]
        forecast2.columns = ['Data', 'Previsão', 'Menor Limite', 'Maior Limite']
        forecast2['Data'] = pd.to_datetime(forecast2['Data']).dt.date
        forecast2 = forecast2.head(days)
        forecast2 = forecast2.reset_index(drop=True)
        pd.set_option('display.max_columns', 4)
        pd.set_option('display.max_rows', days)
        st.dataframe(forecast2, width=650)

    with col4:
        st.write('### Real x Previsão')
        fig1 = model.plot(forecast, xlabel='Data', ylabel='Preço do Petróleo Brent (US$)')
        st.pyplot(fig1, use_container_width=True)

    if not forecast_real.empty:
        wmape = calcula_wmape(forecast_real['y'], forecast.loc[forecast['ds'].isin(forecast_real['ds']), 'yhat'])

        st.info(f'WMAPE do modelo para o intervalo selecionado: {wmape:.2%}')
    else:
        st.write("Não há valores reais para comparar com as previsões.")

    st.write(f'### Previsão de {days} dias')
    fig2 = px.line(forecast.tail(days), x='ds', y='yhat', labels={'yhat': 'Preço do Petróleo Brent (US$)', 'ds': 'Data'})
    st.plotly_chart(fig2)


def calcula_wmape(y_true, y_pred):
    return np.abs(y_true - y_pred).sum() / np.abs(y_true).sum()


main()  