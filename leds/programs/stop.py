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
    while True:
        # Comment this line out if you have RGBW/GRBW NeoPixels
        pixels.fill(BLACK)
        pixels.show()
        time.sleep(10)
