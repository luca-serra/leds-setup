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
    pixels.fill(BLACK)
    pixels.show()
    i = 0
    while True:
        colors = {
            idx: color
            for idx, color in enumerate([RED, GREEN, BLUE, PURPLE, PINK, ORANGE, CYAN, MAGENTA])
        }
        color_indices = list(range(len(colors)))
        color_idx = get_random_element_from_list(color_indices, color_idx)
        elements = WALL + EDGE if i % 2 == 0 else SHELF + TOP
        fill_list(pixels, elements, colors[color_idx])
        pixels.show()
        time.sleep(0.5)
        pixels.fill(BLACK)
        pixels.show()
        i += 1
