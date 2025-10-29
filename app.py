import streamlit as st
st.title("Ejemplo para usar session_state")

count=0

increment = st.button("Increment")
if increment:
  count += 1,1000
st.write("Count = ", count)
