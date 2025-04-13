import streamlit as st
import pydeck as pdk


st.title("Hello World 👋")
st.markdown(
    """ 
    git add streamlit_app.py
git commit -m "Mise à jour de l'application Streamlit"
git push origin main
    """
)

if st.button("Send balloons!"):
    st.balloons()

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=48.85,
        longitude=2.333333,
        zoom=50,
        pitch=20,
    ),
layers=[
  pdk.Layer(
            'ScatterplotLayer',
            
            data=[
                {'position': [2.333333, 48.85], 'size': 1},
               
            ],
            get_color='[200, 30, 0, 160]',
            get_radius=5        ),
],
    ))