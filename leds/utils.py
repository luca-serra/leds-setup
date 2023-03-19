import random
from typing import List, Tuple
import neopixel


def fill_list(pixels: neopixel.NeoPixel, leds: List[int], color: Tuple[int, int, int]):
    for led in leds:
        pixels[led] = color


def get_random_element_from_list(list: List[int], previous_element) -> int:
    element = random.choice(list)
    if element != previous_element:
        return element
    return get_random_element_from_list(list, previous_element)


def get_random_number_from_range(start: int, end: int) -> int:
    return random.randint(start, end)


def apply_brightness(color: Tuple[int, int, int], brightness: float) -> Tuple[int, int, int]:
    return tuple(int(color_value * brightness) for color_value in color)
