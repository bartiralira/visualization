import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt

header = st.beta_container()
dataset = st.beta_container()


with header:
    st.title("welcome to my page")
    
with dataset:
    st.header("comecando")
    dataframe = read_csv('Base e-Track Gestão de Tempos Rodoviários Tratamento-tratado.csv',sep=";",decimal=',')
    df=dataframe[['Permanência no Destino (h)', 'Permanência Origem (h)', 'Local TD', "UF Origem", "UF Cliente"]]
    
    sel_col, disp_col = st.beta_columns(2)
    origem=df.groupby(["Local TD","UF Origem"],as_index=False).agg({"Permanência Origem (h)":"mean"})
    df["Permanência Origem (h)"] = df["Permanência Origem (h)"].astype(int)
    #pd.to_numeric(df["Permanência Origem (h)"])
    #df["Permanência no Destino (h)"] = pd.to_numeric(df["Permanência no Destino (h)"])
    #selecao = sel_col.selectbox("Select",origem[["Local TD"]], index=0)
    selecao = sel_col.slider("Select",min_value=0, max_value=15, value=15)
    
    origem= origem[origem["Permanência Origem (h)"].between(0, selecao, inclusive=False)]

    
    #fig = plt.figure(1, figsize=(50, 50))
    fig = px.scatter_3d(origem, x='Permanência Origem (h)', y='UF Origem', z='Local TD',)
    # tight layout
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0),autosize=False,width=800,height=800,)
    #fig.show()
    

    #st.write(origem.head(5))
    st.subheader("Origem")
    st.write(fig)
    #st.write()
