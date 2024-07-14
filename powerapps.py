import streamlit as st



st.set_page_config(
    page_title="PowerAPPs",
    page_icon=":bulb:",
    layout='wide'
)
st.title("PowerAPPs disponibles")
st.subheader('Powered by Jose Vidal',divider='rainbow')

url_linkedin = "https://www.linkedin.com/posts/jfvidalsierra_powerapps-activity-7216715360010461184-YhHj?utm_source=share&utm_medium=member_desktop"
st.write("Recomienda, comenta y comparte en [Linkedin](%s)" % url_linkedin)

col1,col2,col3,col4=st.columns(4)
with col1:
    st.markdown("Cálculo de indexados")
    st.image('images/telemindex.jpg')
    
with col2:
    st.markdown(':rainbow[OMIE a todo color]')
    st.image('images/escalacv.jpg')
    
with col3:
    st.markdown('Compara FIJO vs PVPC')
    st.image('images/fijovspvpc.jpg')

with col4:
    st.markdown('Simula indexados')
    st.image('images/simulindex.jpg')
    
with st.container():
    col1,col2,col3,col4=st.columns(4)
    with col1:
        url1 = "https://telemindexpy-josevidal.streamlit.app/"
        st.write("Calcula los precios medios de indexado con [Telemindex](%s)" % url1)
    with col2:
        url2 = "https://escalacvpy-josevidal.streamlit.app/"
        st.write("Disfruta OMIE a todo color basado en la [Escala Cavero-Vidal](%s)" % url2)
    with col3:
        url3 = "https://fijovspvpcpy-josevidal.streamlit.app/"
        st.write("Calcula el impacto del margen en el Tp [Fijo vs PVPC](%s)" % url3)
    with col4:
        url4 = "https://simulindexpy-josevidal.streamlit.app/"
        st.write("Simula los precios de indexado a un año vista [Simulindex](%s)" % url4)