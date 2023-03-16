from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Wordd"}


@app.get("/programs/{program_name}")
async def get_program(program_name: str):
    exec(f"from leds.{program_name} import main")
    # TODO: run this in a separate thread
    exec("main()")

    return {"Program started": program_name}
