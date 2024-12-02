import streamlit as st
from util.layout import layout
import pandas as pd

# Define a configuração do app

st.set_page_config(
        page_title='Tech Challenge 04', layout='wide',
        page_icon='📈'
    )

with open('./assets/css/style.css') as s:
    st.markdown(f'<style>{s.read()}</style>', unsafe_allow_html=True)

layout()
