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


def wheel(pos: int) -> Tuple[int, int, int]:
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)
