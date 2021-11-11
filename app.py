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

selection = st.radio('Escoge uno', ['Segmentación', 'Detección'])
if selection == 'Segmentación':
    st.write('Usted escogió segmentación')
    col1, col2 = st.columns(2)
    img_select=col1.selectbox('Escoger una imagen', ['Piloto_20210216_02_193', 'Imagen 2','Imagen 3','Imagen 4'])
    col1.markdown("""# \n \n """)
    if img_select == 'Piloto_20210216_02_193':
        col2.markdown("""#### Fotografia perteneciente a la finca Piloto""")
        col2.markdown("""Vuelo realizado el dia 16 de Febrero del 2021. Esta finca esta ubicada en las coordenadas [1.348868, -77.204256](https://www.google.com/maps/place/1%C2%B020'55.9%22N+77%C2%B012'15.3%22W/@1.3488734,-77.2064447,745m/data=!3m1!1e3!4m5!3m4!1s0x0:0x0!8m2!3d1.348868!4d-77.204256)""")
        col1.image('imgs\segmentado\Piloto_20210216_02_193\Piloto_20210216_02_193_ndvi_entrada.jpg',caption="Imagen de Entrada")
        col2.image('imgs\segmentado\Piloto_20210216_02_193\Piloto_20210216_02_193_ndvi_p2p.jpg',caption="Imagen de Salida")
        st.markdown("""#### Analisis""")

    if img_select == 'Imagen 2':
        col2.markdown("""Aqui va una reseña de la imagen 2""")
    if img_select == 'Imagen 3':
        col2.markdown("""Aqui va una reseña de la imagen 3""")
    if img_select == 'Imagen 4':
        col2.markdown("""Aqui va una reseña de la imagen 4""")
if selection == 'Detección':
    st.write('Usted escogió detección')
    col1, col2 = st.columns(2)
    col1.selectbox('Escoger una imagen', ['Imagen 1', 'Imagen 2','Imagen 3','Imagen 4'])
    col2.write("This is column 2")


## TODO
# Falta desarrollar analisis a la imaen de piloto1 y agregar mas ejemplos
