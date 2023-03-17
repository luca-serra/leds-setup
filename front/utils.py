import requests
import os


def get_server_programs():
    program_names = (
        requests.get(f"{os.environ.get('HOST')}:{os.environ.get('SERVER_PORT')}/programs")
        .json()
        .get("programs")
    )
    return program_names
