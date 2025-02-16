import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
df = pd.read_csv('vehicles_us.csv')
st.header('Car Sales Dashboard')
fig_hist = px.histogram(df, x='odometer', y='price', color ='condition', title='Odometer vs Price')
st.plotly_chart(fig_hist)
st.header('Year vs Price')
fig_scatter= px.scatter(df, x='model_year', y='price', color ='condition', title='Year vs Price')
st.plotly_chart(fig_scatter)
df['manufacturer'] = df['model'].str.split().str[0]
df_automatic = df[df['transmission'] =='automatic']
df_manual = df[df['transmission'] =='manual']

agree = st.checkbox('If automatic transmission is preferred')
if agree:
    st.write('Automatic transmission is preferred')
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_automatic['manufacturer'], nbinsx=50, name='Automatic', marker_color='blue'))
    fig.add_trace(go.Histogram(x=df_manual['manufacturer'], nbinsx=50, name='Manual', marker_color='orange'))
    fig.update_layout(
        xaxis_title='Manufacturer',
        yaxis_title='Number of Cars',
        title='Distribution by Transmission Type',
        legend_title='Transmission Type',
        barmode='overlay'
    )
    fig.update_traces(opacity=0.75)
    st.plotly_chart(fig)