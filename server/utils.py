import os


def get_all_programs():
    program_names = [
        file.replace(".py", "") for file in os.listdir("./leds/programs") if file.endswith(".py")
    ]
    return program_names
