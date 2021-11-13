# Librerias
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

## -----------------------------------
## Funciones

def mas_informacion(nombre,latitud,longitud,area=[30, 30, 40]):
        st.markdown("""Estas son las fotografias multiespectrales para la imagen **{imagen}**""".format(imagen=nombre))
        c1,c2,c3,c4,c5 = st.columns(5)        
        c1.image('imgs/segmentado/{imagen}/{imagen}_b1_entrada.jpg'.format(imagen=nombre),caption="Banda Verde, longitud de onda 550nm")
        c2.image('imgs/segmentado/{imagen}/{imagen}_b2_entrada.jpg'.format(imagen=nombre),caption="Banda Roja, longitud de onda 660nm")
        c3.image('imgs/segmentado/{imagen}/{imagen}_b3_entrada.jpg'.format(imagen=nombre),caption="Banda Borde Rojo, longitud de onda 735nm")
        c4.image('imgs/segmentado/{imagen}/{imagen}_b4_entrada.jpg'.format(imagen=nombre),caption="Banda Infrarroja, longitud de onda 790nm")
        c5.image('imgs/segmentado/{imagen}/{imagen}_gray.jpg'.format(imagen=nombre),caption="Imagen de referencia en escala de grises")
        st.markdown("""#### Segmentación de áreas """)
        c1,c2=st.columns([2, 3])
        with c1:
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = ['Baja', 'Media', 'Alta']
            sizes = area
            explode = (0, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
            #add colors
            colors = ['#66b3ff','#99ff99','#ff9999']
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            #draw circle
            centre_circle = plt.Circle((0,0),0.50,fc='white')
            fig = plt.gcf()
            fig.gca().add_artist(centre_circle)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig1)
        with c2:
            texto = """
            Para la imagen **{imagen}** se encuentra una segmentación de:
            * {bajo}% del área en la imagen como una claisifcación "baja" 
            * {medio}% del área en la imagen como una claisifcación "media"
            * {alto}% del área en la imagen como una claisifcación "alta"
            """.format(imagen=nombre,bajo=area[0],medio=area[1],alto=area[2])
            st.markdown(texto)
        with st.expander("Mas detalles sobre clasificaciones"):
            texto="""
                La región que encierra la imagen seleccionada es analizada por el algoritmo de inteligencia artificial y segmentada en 3 clasificaciones distintas
                * **Bajo**: Esta clasificación muestra una área que contenga muy baja actividad fotosintetica o inclusive sea infraestructura artificial, tales como carreteras, edificaciones, entre otros.
                * **Medio**: Esta clasificación muestra vegetación que tiene una actividad fotosintetica moderada, es decir la vitalidad de la vegetación esta en un termino medio.
                * **Alto**: Esta clasificación muestra una vegetación con alta actividad fotosintetica, es decir una vegetacion en óptimas condiciones para su crecimiento y producción.
            """
            st.write(texto)
            st.image("imgs/cafe-planta.jpg")
        st.markdown("""#### Ubicación Geográfica""")
        df = pd.DataFrame(np.zeros([1, 2]) + [latitud, longitud],columns=['lat', 'lon'])
        st.map(df,11)
## Fin funciones
##-----------------------------------


# -----------------------------------------------------------
# CODIGO
st.title('.')
st.image('imgs/IntroTesisColor Cafe.png')
# uploaded_file = st.file_uploader('Subir Imagen',accept_multiple_files=False,type="jpg")
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption='Uploaded Image.', use_column_width=False,width=200)

selection = st.selectbox('Seleccionar una opción', ['Seleccionar','Segmentación', 'Detección'])

if selection == 'Segmentación':
    st.write('Usted escogió segmentación')
    col1, col2 = st.columns(2)
    img_select=col1.selectbox('ESCOGER UNA IMAGEN', ['Piloto_20210216_02_193', 'LaMina_20210320_02_70','LomaGorda_20210320_02_49','ElArrayan_20210612_01_35'])
    col1.markdown("""# \n \n """)
    col1.markdown("""# \n \n """)
    if img_select == 'Piloto_20210216_02_193':
        col2.markdown("""#### Fotografia perteneciente a la finca Piloto""")
        col2.markdown("""Vuelo realizado el dia 16 de Febrero del 2021. Esta finca esta ubicada en las coordenadas [1.348868, -77.204256](https://www.google.com/maps/place/1%C2%B020'55.9%22N+77%C2%B012'15.3%22W/@1.3488734,-77.2064447,745m/data=!3m1!1e3!4m5!3m4!1s0x0:0x0!8m2!3d1.348868!4d-77.204256)""")
        col1.image('imgs/segmentado/Piloto_20210216_02_193/Piloto_20210216_02_193_ndvi_entrada.jpg',caption="Imagen de Entrada NDVI")
        col2.image('imgs/segmentado/Piloto_20210216_02_193/Piloto_20210216_02_193_ndvi_p2p.jpg',caption="Imagen de Salida")
        st.markdown("""---""")
        st.markdown("""### Mas Información""")
        mas_informacion('Piloto_20210216_02_193',latitud=1.348868,longitud=-77.204256,area=[11.1,35.1,53.8])

    if img_select == 'LaMina_20210320_02_70':
        col2.markdown("""#### Fotografia perteneciente a la finca La Mina""")
        col2.markdown("""Vuelo realizado el dia 20 de Marzo del 2021. Esta finca esta ubicada en las coordenadas [1.3551194,-77.15594722 ](https://www.google.com/maps/place/1%C2%B021'18.4%22N+77%C2%B009'21.4%22W/@1.3551248,-77.1581359,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x5deb3acd86fec4a2!8m2!3d1.3551194!4d-77.1559472?hl=es)""")
        col1.image('imgs/segmentado/{name}/{name}_ndvi_entrada.jpg'.format(name=img_select),caption="Imagen de Entrada NDVI")
        col2.image('imgs/segmentado/{name}/{name}_ndvi_p2p.jpg'.format(name=img_select),caption="Imagen de Salida")
        st.markdown("""---""")
        st.markdown("""### Mas Información""")
        mas_informacion(img_select,latitud=1.3551194,longitud=-77.15594722,area=[2.5,40.94,52.6])

    if img_select == 'LomaGorda_20210320_02_49':
        col2.markdown("""#### Fotografia perteneciente a la finca Loma Gorda""")
        col2.markdown("""Vuelo realizado el dia 20 de Marzo del 2021. Esta finca esta ubicada en las coordenadas [1.3621556,-77.15957222](https://www.google.com/maps/place/1%C2%B021'43.8%22N+77%C2%B009'34.5%22W/@1.362161,-77.1617609,745m/data=!3m2!1e3!4b1!4m5!3m4!1s0x0:0x8269e41e0b34f66e!8m2!3d1.3621556!4d-77.1595722?hl=es)""")
        col1.image('imgs/segmentado/{name}/{name}_ndvi_entrada.jpg'.format(name=img_select),caption="Imagen de Entrada NDVI")
        col2.image('imgs/segmentado/{name}/{name}_ndvi_p2p.jpg'.format(name=img_select),caption="Imagen de Salida")
        st.markdown("""---""")
        st.markdown("""### Mas Información""")
        mas_informacion(img_select,latitud=1.3621556,longitud=-77.15957222,area=[19.5,28.61,51.96])
        
    if img_select == 'ElArrayan_20210612_01_35':
        col2.markdown("""#### Fotografia perteneciente a la finca Loma Gorda""")
        col2.markdown("""Vuelo realizado el dia 20 de Marzo del 2021. Esta finca esta ubicada en las coordenadas [1.3957833,-77.120375](https://www.google.com/maps/place/1%C2%B023'44.8%22N+77%C2%B007'13.4%22W/@1.3957887,-77.1225637,745m/data=!3m2!1e3!4b1!4m5!3m4!1s0x0:0xbef737715d0fa76!8m2!3d1.3957833!4d-77.120375?hl=es)""")
        col1.image('imgs/segmentado/{name}/{name}_ndvi_entrada.jpg'.format(name=img_select),caption="Imagen de Entrada NDVI")
        col2.image('imgs/segmentado/{name}/{name}_ndvi_p2p.jpg'.format(name=img_select),caption="Imagen de Salida")
        st.markdown("""---""")
        st.markdown("""### Mas Información""")
        mas_informacion(img_select,latitud=1.3957833,longitud=-77.120375,area=[21.3,39.6,39.1])
    
if selection == 'Detección':
    st.write('Usted escogió detección')
    col1, col2 = st.columns(2)
    col1.selectbox('Escoger una imagen', ['Imagen 1', 'Imagen 2','Imagen 3','Imagen 4'])
    col2.write("This is column 2")


## TODO
# Falta desarrollar analisis a la imaen de piloto1 y agregar mas ejemplos
