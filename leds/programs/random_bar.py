import time
import board
import neopixel
from leds.config.colors import BLACK, RED, GREEN, BLUE, WHITE, PURPLE, PINK, ORANGE, CYAN, MAGENTA
from leds.config.positions import WALL, SHELF, EDGE, TOP
from leds.utils import fill_list, get_random_element_from_list
from leds.config.positions import NUM_PIXELS


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, NUM_PIXELS, brightness=0.2, auto_write=False, pixel_order=ORDER
)
if __name__ == "__main__":
    element_idx = 0
    color_idx = 0
    while True:
        pixels.fill(BLACK)
        pixels.show()
        time.sleep(0.05)
        elements = {0: WALL, 1: SHELF, 2: EDGE, 3: TOP}
        colors = {
            idx: color
            for idx, color in enumerate([RED, GREEN, BLUE, PURPLE, PINK, ORANGE, CYAN, MAGENTA])
        }
        element_indices = list(range(len(elements)))
        color_indices = list(range(len(colors)))
        element_idx = get_random_element_from_list(element_indices, element_idx)
        color_idx = get_random_element_from_list(color_indices, color_idx)
        fill_list(pixels, elements[element_idx], colors[color_idx])
        pixels.show()
        time.sleep(0.5)
