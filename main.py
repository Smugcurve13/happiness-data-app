import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('happy.csv')

st.title("In Search For Happiness")

xaxis = st.selectbox("Select the Data for X-Axis",['gdp','happiness','generosity'])
yaxis = st.selectbox("Select the Data for Y-Axis",['gdp','happiness','generosity'])

st.subheader(f'{xaxis.title()} and {yaxis.title()}')

figure = px.scatter(df, x=xaxis,y=yaxis,labels={'x':xaxis.title(),'y':yaxis.title})
st.plotly_chart(figure)