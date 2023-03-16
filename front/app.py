import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()


st.markdown(
    """<p align="center" style="color:#FF6F17;background-color:#FAD7A0">Coucou joli chat ! :).</p>""",
    unsafe_allow_html=True,
)

program_names = (
    requests.get(f"{os.environ.get('HOST')}:{os.environ.get('SERVER_PORT')}/programs")
    .json()
    .get("programs")
)

for program_name in program_names:
    st.button(program_name)
