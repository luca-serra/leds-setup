import time
import board
import neopixel
from leds.config.colors import BLACK, RED, GREEN, BLUE, WHITE, PURPLE, PINK, ORANGE, CYAN, MAGENTA
from leds.config.positions import SHELF, TOP
from leds.config.positions import NUM_PIXELS
from leds.utils import fill_list, wheel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, NUM_PIXELS, brightness=0.6, auto_write=False, pixel_order=ORDER
)
if __name__ == "__main__":
    count = 0
    while True:
        fill_list(pixels, SHELF + TOP, wheel(count % 255))
        pixels.show()
        time.sleep(0.4)
        count += 1
