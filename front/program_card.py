import os
import requests
import streamlit as st


def build_program_card(program_name: str) -> None:
    def _on_click_program_card() -> None:
        requests.get(
            f"{os.environ.get('HOST')}:{os.environ.get('SERVER_PORT')}/programs/{program_name}"
        )

    st.button(program_name, key=program_name, on_click=_on_click_program_card)
