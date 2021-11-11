# Librerias
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

# CODIGO
st.image('imgs/IntroTesisColor Cafe.png')
# uploaded_file = st.file_uploader('Subir Imagen',accept_multiple_files=False,type="jpg")
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption='Uploaded Image.', use_column_width=False,width=200)

selection = st.radio('Escoger uno', ['Segmentación', 'Detección'])
if selection == 'Segmentación':
    st.write('Usted escogió segmentación')
if selection == 'Detección':
    st.write('Usted escogió detección')
