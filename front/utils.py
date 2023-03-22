from typing import List
import requests
import os


def get_server_programs() -> List[str]:
    program_names = (
        requests.get(f"{os.environ.get('HOST')}:{os.environ.get('SERVER_PORT')}/programs")
        .json()
        .get("programs")
    )
    return program_names


def get_friendly_program_name(program_name: str) -> str:
    return program_name.replace("_", " ").capitalize()
