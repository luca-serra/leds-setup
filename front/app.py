import streamlit as st
import requests


st.markdown(
    """<p align="center" style="color:#FF6F17;background-color:#FAD7A0">Coucou joli chat ! :).</p>""",
    unsafe_allow_html=True,
)

program_names = requests.get("http://192.168.1.21:8000/pr").json().get("programs")

for program_name in program_names:
    st.button(program_name)
