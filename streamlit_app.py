import streamlit as st

st.title("Convertidor de temperatura")

temp_c = st.slider("Indica la temperatura", 0, 100)

temp_f = (temp_c * 9/5) + 32

st.write(temp_f)
