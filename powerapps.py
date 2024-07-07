import streamlit as st



st.set_page_config(
    page_title="PowerAPPs",
    page_icon=":bulb:",
    layout='centered'
)
st.title("PowerAPPs disponibles")
st.subheader("Powered by Jose Vidal")

url_linkedin = "https://www.linkedin.com/in/jfvidalsierra/"
st.write("Visita mi perfil de  [Linkedin](%s)" % url_linkedin)

col1,col2=st.columns(2)
with col1:
    st.image('images/telemindex.jpg',caption='Cálculo de precios de indexado')
    url1 = "https://escalacvpy-josevidal.streamlit.app/"
    st.write("Calcula los precios medios de indexado con [Telemindex](%s)" % url1)
    #st.page_link('https://telemindexpy-josevidal.streamlit.app/', label = 'Telemindex')
with col2:
    st.image('images/escalacv.jpg',caption='Omie a todo color')
    url2 = "https://escalacvpy-josevidal.streamlit.app/"
    st.write("Disfruta OMIE a todo color basado en la [Escala Cavero-Vidal](%s)" % url2)
    #st.markdown("check out this [link](%s)" % url2)
    #st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)")
    #st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)")