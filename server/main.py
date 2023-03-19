import os
from fastapi import FastAPI

from server.utils import get_all_programs
from loguru import logger

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
    logger.info("Kill python scripts running...")
    os.system("sudo kill -9 $(pgrep -f 'python3 leds/')")
    logger.info(f"Starting program: {program_name}")
    os.system(f"sudo python3 leds/programs/{program_name}.py &")
    return {"Program started": program_name}
