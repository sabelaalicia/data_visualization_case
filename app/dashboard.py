import streamlit as st
import os
ruta_actual = os.getcwd()
ruta_actual = ruta_actual.replace('\\', '//')
ruta_actual = ruta_actual.rsplit('//', 1)[0]


st.set_page_config(layout="wide")
st.title("Incendios forestales en España. Contextualización.")
st.markdown("""
Los incendios forestales no son solo llamas que arrasan bosques: son una amenaza para la naturaleza, los animales, las personas y el clima.  
En este panel interactivo podrás explorar cómo han evolucionado los incendios en España, cuántos se han producido, en qué zonas han sido más frecuentes y qué factores pueden influir en su aparición.

Porque proteger los bosques es proteger nuestro futuro. 🌍💚
""")
path_html = ruta_actual+"\\images\\html\\"
path_png=  ruta_actual+"\\images\\png\\"

tabs = st.tabs(["¿Qué es un incendios forestal?", "¿Dónde y cuándo?", "El suelo", "La gente", "El clima", "Otros factores"])

# TAB 1 - ¿Qué es un incendio forestal?
with tabs[0]:
    col1,col2=col1, col2 = st.columns([3, 2]) 
    with col1:
        st.markdown("""
        #### ¿Qué es un incendio forestal?
        Un incendio forestal es un fuego que se produce en áreas con bosques, matorrales o plantas, y que puede extenderse rápidamente, consumiendo árboles, animales y todo lo que encuentra a su paso.

        Los incendios forestales causan graves daños al medio ambiente: destruyen la vegetación, ponen en peligro la vida de los animales y pueden afectar a las personas cercanas. Además, liberan grandes cantidades de gases y partículas contaminantes al aire, que contribuyen al cambio climático y pueden afectar nuestra salud.

        #### ¿Por qué es importante conocer el contexto en el que ocurren?

        Entender las condiciones del clima y las emisiones en el momento en que se produce un incendio nos ayuda a descubrir qué factores influyen en su aparición y propagación. Esta información es fundamental para mejorar la prevención, la detección temprana y la gestión de los incendios forestales, protegiendo así nuestros bosques y la calidad de vida de todos.
        """)
    with col2:
         st.image(path_png + "imagen_incendio.jpg", caption="Inceidos Forestal en la provincia de Zamora en 2022 con mas de 50.000 hectáreas calcinadas.", use_container_width=True)


# TAB 2 - ¿Dónde y cuándo?
with tabs[1]:
    st.subheader("¿Dónde y cuándo han ocurrido los incendios?")
    st.markdown("""
        En el mapa de la izquierda observamos que la mayoría de los incendios se concentran en la zona norte de la península. ¡Esto no significa que sea un problema exclusivo de Galicia! Los incendios provocan devastación en toda la geografía española. Sin embargo, el problema es especialmente grave en las regiones del norte de España.

        En la gráfica de la derecha vemos cómo, lejos de disminuir, el número de incendios ha aumentado desde que se tienen registros hasta principios de los años 2000.

        Si tienes curiosidad por conocer mejor los datos de tu provincia o de otra región, utiliza el gráfico de abajo para ver la evolución anual de incendios en cada provincia. 🔍
        """)
    col1, col2 = st.columns(2)

    with col1:
        st.image(path_png + "mapaIncendiosPorProvincia.png", caption="Mapa de incendios por provincia", use_container_width =True)
    
    with col2:
        st.image(path_png + "evol_incedios.png", caption="Incendios por mes", use_container_width =True)

    with open(path_html + "incendios_comunidad.html", "r", encoding="utf-8") as f:
        html_content = f.read()
        st.components.v1.html(html_content, height=600)
# TAB 3 - El suelo
with tabs[2]:
    st.subheader("¿Qué hay donde se inician los incendios?")
    st.markdown("""
    En el mapa de la izquierda podemos ver cómo evoluciona el tipo de suelo en España desde los años 90. En la leyenda puedes leer a qué hace referencia cada color, pero puedes quedarte con esta idea:

    - 🌳 Verdes: zonas con vegetación natural  
    - 🌾 Amarillos: zonas con vegetación cultivada  
    - 🟫 Marrones: zonas con vegetación artificial  
    - 🌸 Rosas: zonas urbanas
    - ⚫ Negros: zonas quemadas

    Con estos datos, vamos a ver dónde se han producido más incendios. Hemos agrupado en categorías generales y podemos observar que una gran parte de los incendios se inician en **áreas urbanas** y **tierras de cultivo**.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.video(path_png+"evol_suelo.mp4")

    with col2:
        with open(path_html + "tipo_suelo_pie.html", "r", encoding="utf-8") as f:
            html_content = f.read()
            st.components.v1.html(html_content, height=600)

# TAB 4 - La gente
with tabs[3]:
    st.subheader("¿Cuántas personas hay donde ocurren estos incendios?")
    st.markdown(""" También es importante conocer cuánta gente vive alrededor de los incendios. ¿Zonas altamente pobladas? ¿O regiones vacías? Vamos a dividir todas las provincias en:
    
    -  Urbanas (azul)  
    -  Semiurbanas (amarillo)  
    -  Rurales (rosa)  
                
    En la gráfica de la izquierda tenemos una distribución general de los incendios, mientras que en la derecha podemos ver con más detalle cómo esta distribución va cambiando a lo largo de los años.  """)
    col1, col2 = st.columns(2)

    with col1:
            with open(path_html + "pie_zonas.html", "r", encoding="utf-8") as f:
                html_content = f.read()
                st.components.v1.html(html_content, height=600)
    with col2:
            with open(path_html + "zonas_evol.html", "r", encoding="utf-8") as f:
                html_content = f.read()
                st.components.v1.html(html_content, height=600)

# TAB 5 - El clima
with tabs[4]:
    st.subheader("¿Qué clima hay donde ocurren estos incendios?")
    st.markdown("""
    El clima es uno de los factores clave que influyen en la ocurrencia y propagación de los incendios forestales.  
    En esta sección analizaremos las condiciones climáticas en las zonas afectadas por los incendios, como temperatura, humedad y precipitación.  
    Entender el clima nos ayudará a identificar patrones y periodos de mayor riesgo, así como a diseñar estrategias más efectivas de prevención y gestión. 🌡️🌧️🔥

    En los tres mapas podemos observar cómo los incendios se concentran en las regiones más frías y húmedas. Esto puede parecer contraintuitivo, pero se entiende mejor cuando revisamos las dos gráficas de abajo. En ellas podemos ver que los incendios tienen un carácter muy estacional y se acumulan en los meses con menos precipitaciones y humedad.
    """)

    
    col1, col2,col3 = st.columns(3)

    with col1:
        st.image(path_png + "mapaIncendiosPorProvincia.png", caption="Mapa de incendios por provincia", use_container_width =True)
    
    with col2:
        st.image(path_png + "mapa_temp.png", caption="Temperatura media por provincia", use_container_width =True)
    with col3:
        st.image(path_png + "precipitacion_prov.png", caption="Precipitación media por provincia", use_container_width =True)

    # Segunda fila con 2 imágenes
    col1, col2 = st.columns(2)
    with col1:
        st.image(path_png + "hum_mensual.png", caption="Relación entre humedad e incendios a los largo de las estaciones.", use_container_width=True)
    with col2:
        st.image(path_png + "prec_mensual.png", caption="Relación entre precipitación e incendios a los largo de las estaciones.", use_container_width=True)

# TAB 6 - Otros factores
with tabs[5]: 
    st.subheader("Gases de efecto invernadero")
    col1,col2=col1, col2 = st.columns([3, 2]) 
    with col1:
        st.markdown("""
        Los gases de efecto invernadero son una de las principales causas del cambio climático, el cual provoca el aumento de las temperaturas y las sequías, entre otros efectos. Como vimos en la sección **El Clima**, los períodos anuales con altas temperaturas y baja humedad son los más propicios para la ocurrencia de incendios.

        En la figura de al lado podemos observar una gráfica que compara las emisiones y la cantidad anual de incendios. En ella se aprecia que no existe una relación lineal clara entre ambos factores, debido a que el cambio climático es un fenómeno mucho más complejo.

        Que no exista una relación lineal no significa que los dos conceptos no estén relacionados. Debemos preocuparnos por reducir las emisiones para conseguir, entre otras muchas cosas, que las condiciones de temperatura y humedad que favorecen los incendios no aumenten.

        En el gráfico de abajo se muestra cómo las emisiones de gases de efecto invernadero han aumentado a lo largo de los años.
        """)

    with col2:
         st.image(path_png + "disp_emisiones.png", use_container_width=True)
    with open(path_html + "evol_ems.html", "r", encoding="utf-8") as f:
            html_content = f.read()
            st.components.v1.html(html_content, height=600)