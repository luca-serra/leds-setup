import os

from fastapi import FastAPI

from server.utils import get_all_programs


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome"}


@app.get("/programs")
async def get_programs():
    programs = get_all_programs()
    return {"programs": programs}


@app.get("/programs/{program_name}")
async def run_program(program_name: str):
    # TODO: run this in a separate thread?
    os.system(f"sudo python3 leds/{program_name}.py")

    return {"Program started": program_name}
