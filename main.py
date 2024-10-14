import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search For Happiness")

xaxis = st.selectbox("Select the Data for X-Axis",['GDP','Happiness','Generosity'])
yaxis = st.selectbox("Select the Data for Y-Axis",['GDP','Happiness','Generosity'])

df = pd.read_csv('happy.csv')


match xaxis:
    case "GDP":
        x_array = df['gdp']
    case "Happiness":
        x_array = df['happiness']    
    case "Generosity":
        x_array = df['generosity']

match yaxis:
    case "GDP":
        y_array = df['gdp']
    case "Happiness":
        y_array = df['happiness']    
    case "Generosity":
        y_array = df['generosity']

print(xaxis,yaxis)


st.subheader(f'{xaxis} and {yaxis}')

figure = px.scatter(df, x=x_array,y=y_array,labels={'x':xaxis,'y':yaxis})
st.plotly_chart(figure)