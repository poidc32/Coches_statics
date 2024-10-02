import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('C:/Users/Olagu/OneDrive/Escritorio/TRIPLE_TEN/SPRINT_6/Coches_statics/vehicles_us.csv') 
st.header('Vehiculos en estados unidos') #encabezado

build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificacion esta seleccionada
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter: 
            
            st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
            fig_st = px.scatter(car_data, x="odometer", y="price")
        
            st.plotly_chart(fig_st, use_container_width=True)