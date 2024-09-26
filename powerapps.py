import streamlit as st



st.set_page_config(
    page_title="PowerAPPs",
    page_icon=":bulb:",
    layout='wide'
)
st.title('PowerAPPs disponibles by Jose Vidal')
#st.subheader('Powered by Jose Vidal',divider='rainbow')

url_linkedin = "https://www.linkedin.com/posts/jfvidalsierra_powerapps-activity-7216715360010461184-YhHj?utm_source=share&utm_medium=member_desktop"
st.write("Recomienda, comenta y comparte en [Linkedin](%s)" % url_linkedin)

col11,col12,col13,col14=st.columns(4)
with col11:
    #st.markdown("Cálculo de indexados")
    url1 = "https://telemindex-josevidal.streamlit.app/"
    st.subheader('Telemindex',divider='rainbow')
    st.write("Calcula los precios medios de indexado con [Telemindex](%s)" % url1)
    st.image('images/telemindex.jpg')
    
with col12:
    #st.markdown(':rainbow[OMIE a todo color]')
    url2 = "https://escalacvpy-josevidal.streamlit.app/"
    st.subheader('Escala Cavero-Vidal',divider='rainbow')
    st.write("Disfruta de :rainbow[OMIE a todo color] basado en la [Escala Cavero-Vidal](%s)" % url2)
    st.image('images/escalacv.jpg')
    
with col13:
    #st.markdown('Compara FIJO vs PVPC')
    url3 = "https://fijovspvpcpy-josevidal.streamlit.app/"
    st.subheader('Compara fijo vs PVPC',divider='rainbow')
    st.write("¿Ganas o pierdes?: Compara tu [Fijo vs PVPC](%s)" % url3)
    st.image('images/fijovspvpc.jpg')

with col14:
    #st.markdown('Simula indexados')
    url4 = "https://simulindexpy-josevidal.streamlit.app/"
    st.subheader('Simulindex',divider='rainbow')
    st.write("Simula el precio medio de indexado a un año vista con [Simulindex](%s)" % url4)
    st.image('images/simulindex.jpg')
    
#with st.container():
#    col21,col22,col23,col24=st.columns(4)
    #with col21:
    #    url1 = "https://telemindex-josevidal.streamlit.app/"
    #    st.write("Calcula los precios medios de indexado con [Telemindex](%s)" % url1)
    #with col22:
    #    url2 = "https://escalacvpy-josevidal.streamlit.app/"
    #    st.write("Disfruta OMIE a todo color basado en la [Escala Cavero-Vidal](%s)" % url2)
    #with col23:
    #    url3 = "https://fijovspvpcpy-josevidal.streamlit.app/"
    #    st.write("Calcula el impacto del margen en el Tp [Fijo vs PVPC](%s)" % url3)
    #with col24:
    #    url4 = "https://simulindexpy-josevidal.streamlit.app/"
    #    st.write("Simula los precios de indexado a un año vista [Simulindex](%s)" % url4)

col31,col32,col33,col34=st.columns(4)
with col31:
    #st.markdown("Demanda Real")
    url5 = "https://demanda-josevidal.streamlit.app/"
    st.subheader('Demanda Real',divider='rainbow')
    st.write("Simula la [demanda real](%s). Se incluye producción por autoconsumo" % url5)
    st.image('images/demanda.jpg')
with col32:
    #st.markdown("Marginales")
    url6 = "https://marginales-by-josevidal.streamlit.app/"
    st.subheader('Tecnologías Marginales',divider='rainbow')
    st.write("Impacto de las tecnologías [marginales](%s) en el precio del mercado" % url6)
    st.image('images/marginales.jpg')
with col33:
    #st.markdown("Excedentes")
    url7 = "https://excedentes-josevidal.streamlit.app/"
    st.subheader('Autoconsumo: Excedentes',divider='rainbow')
    st.write("Compara el coste regulado de tus [excedentes](%s) con la oferta en fijo" % url7)
    st.image('images/excedentes.jpg')


#with st.container():
#    col41,col42,col43,col44=st.columns(4)
    #with col41:
    #    url5 = "https://demanda-josevidal.streamlit.app/"
    #    st.write("Simula la demanda real [Demanda](%s)" % url5)
    #with col42:
    #    url6 = "https://marginales-by-josevidal.streamlit.app/"
    #    st.write("Impacto de las tecnologías [marginales](%s) en el precio del mercado" % url6)
    #with col43:
    #    url7 = "https://excedentes-josevidal.streamlit.app/"
    #    st.write("Calcula tus [excedentes](%s) en la tarifa regulada" % url7)