import os

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome"}


@app.get("/pr")
async def programs():
    programs = [file.replace(".py", "") for file in os.listdir("./leds/") if file.endswith(".py")]
    return {"programs": programs}


@app.get("/programs/{program_name}")
async def run_program(program_name: str):
    # TODO: run this in a separate thread?
    os.system(f"sudo python3 leds/{program_name}.py")

    return {"Program started": program_name}
