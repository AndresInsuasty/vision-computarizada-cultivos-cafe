# Librerias
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

# CODIGO
st.title('Sistema de Visión Computarizada con Inteligencia Artificial para Extraer Información de Cultivos de Café en el Sur Occidente Colombiano')
st.text('Creado por: Andres Insuasty')
st.image('imgs/Generador U-Net.png')
uploaded_file = st.file_uploader('Subir Imagen',accept_multiple_files=False,type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=False,width=200)

## TODO
# crear un boton para seleccionar deteccion de objetos y segmentacion de objetos