import os
import requests
import streamlit as st

from front.utils import get_friendly_program_name


def build_program_card(program_name: str) -> None:
    def _on_click_program_card() -> None:
        requests.get(
            f"{os.environ.get('HOST')}:{os.environ.get('SERVER_PORT')}/programs/{program_name}"
        )

    program_name_display = get_friendly_program_name(program_name)
    st.button(program_name_display, key=program_name, on_click=_on_click_program_card)
