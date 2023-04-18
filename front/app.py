import streamlit as st
from dotenv import load_dotenv
from front.program_card import build_program_card

from front.utils import get_server_programs

load_dotenv()

from PIL import Image

img = Image.open("resources/photo.jpeg")

st.markdown(
    """<p align="center" style="color:black;background:linear-gradient(to bottom, #FCD8F9 0%, #FFFFFF 100%);">Bienvenue chez ChaFrench et ABP !</p>""",
    unsafe_allow_html=True,
)
st.image(img, use_column_width=True)
st.markdown(
    """<p align="center" style="color:black;background:linear-gradient(to bottom, #FCD8F9 0%, #FFFFFF 100%);">Voici la liste des programmes disponibles sur le serveur :</p>""",
    unsafe_allow_html=True,
)
st.markdown(
    """
        <style>
        div.stButton > button:first-child {
        color: #009EAC;
        backgroud-color: ##E0E0E0;
        border: 1px solid #D0D0D0";
        height: 30px;
        width: 90%;
        margin:auto;
        display: block;
        }
        </style>
        """,
    unsafe_allow_html=True,
)
st.markdown(
    """
        <style>
        .css-gf00eh {
            background: linear-gradient(to bottom, #FCD8F9 0%, #FFFFFF 100%);
        }
        .css-d07ibl {
            visibility: hidden;
        }
        .css-hfyt54 {
            visibility: hidden;
        }
        </style>
        """,
    unsafe_allow_html=True,
)

program_names = get_server_programs()

for program_name in program_names:
    build_program_card(program_name)
