import streamlit as st



st.set_page_config(
    page_title="ePowerAPPs",
    page_icon=":bulb:",
    layout='wide'
)
st.title(':orange[e]PowerAPPs© disponibles by Jose Vidal')
url_bluesky = 'https://bsky.app/profile/poweravenger.bsky.social'
#st.markdown("¡Sígueme en [Bluesky](https://bsky.app/profile/poweravenger.bsky.social)!")

url_linkedin = "https://www.linkedin.com/posts/jfvidalsierra_powerapps-activity-7216715360010461184-YhHj?utm_source=share&utm_medium=member_desktop"
url_bluesky = 'https://bsky.app/profile/poweravenger.bsky.social'
#st.write("Recomienda, comenta y comparte en [Bluesky](%s). Gracias a :orange[Jesús López] por el empujoncito con el python." % url_bluesky)
st.markdown(f"Deja tus comentarios y propuestas en mi perfil de [Linkedin]({url_linkedin}) - ¡Sígueme en [Bluesky]({url_bluesky})!")

col11,col12,col13,col14,col15=st.columns(5)
with col11:
    #st.markdown("Cálculo de indexados")
    url1 = "https://minorista-josevidal.streamlit.app/"
    st.subheader('Mercado minorista de la electriciad',divider='rainbow')
    st.write("Toda la información del mercado [minorista](%s)  de la electricidad" % url1)
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


with col15:
    #st.markdown("Demanda + Autoconsumo")
    url5 = "https://demanda-josevidal.streamlit.app/"
    st.subheader('Demanda + Autoconsumo',divider='rainbow')
    st.write("Simula el [CONSUMO](%s) como la demanda más el autoconsumo" % url5)
    st.image('images/demanda.jpg')
    

col21,col22,col23,col24,col25=st.columns(5)
with col21:
    #st.markdown("Marginales")
    url6 = "https://marginales-by-josevidal.streamlit.app/"
    st.subheader('Tecnologías Marginales',divider='rainbow')
    st.write("Impacto de las tecnologías [marginales](%s) en el precio del mercado" % url6)
    st.image('images/marginales.jpg')
with col22:
    #st.markdown("Excedentes")
    url7 = "https://excedentes-josevidal.streamlit.app/"
    st.subheader('Autoconsumo: Excedentes',divider='rainbow')
    st.write("Compara el coste regulado de tus [excedentes](%s) con la oferta en fijo" % url7)
    st.image('images/excedentes.jpg')
#with col23:
#    url8 = "https://omipvsomie-josevidal-superporraomie2024.streamlit.app/"
#    st.subheader('Especial superporreros2024',divider='rainbow')
#    st.write("¿Bates a OMIP en la lucha por el [MVPStarPower2024](%s)?" % url8)
#    st.image('images/omipvsomie.jpg')
with col23:
    url9 = "https://redata-by-josevidal.streamlit.app/"
    st.subheader('Infografías REData',divider='rainbow')
    st.write("Otra forma de ver los datos de [REData](%s)" % url9)
    st.image('images/redata.jpg')
with col14:
    url10 = "https://spo2425-josevidal.streamlit.app/"
    st.subheader('SPO: Super Power OMIE 2024-2025',divider='rainbow')
    st.write("Gana el [MVPStarPower](%s) del año y bate a OMIP!" % url10)
    st.image('images/spo.jpg')

