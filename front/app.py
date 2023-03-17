import streamlit as st
from dotenv import load_dotenv
from front.program_card import build_program_card

from front.utils import get_server_programs

load_dotenv()


st.markdown(
    """<p align="center" style="color:#FF6F17;background-color:#FAD7A0">Coucou joli chat ! :).</p>""",
    unsafe_allow_html=True,
)

program_names = get_server_programs()

for program_name in program_names:
    build_program_card(program_name)
