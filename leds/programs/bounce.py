import time
import board
import neopixel
from leds.config.colors import BLACK, RED, GREEN, BLUE, WHITE, PURPLE, PINK, ORANGE, CYAN, MAGENTA
from leds.config.positions import WALL, SHELF, EDGE, TOP
from leds.utils import (
    apply_brightness,
    get_random_element_from_list,
    get_random_number_from_range,
)
from leds.config.positions import NUM_PIXELS


pixel_pin = board.D18

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, NUM_PIXELS, brightness=0.2, auto_write=False, pixel_order=ORDER
)

colors = {
    idx: color for idx, color in enumerate([RED, GREEN, BLUE, PURPLE, PINK, ORANGE, CYAN, MAGENTA])
}
color_indices = list(range(len(colors)))


class Line:
    def __init__(self):
        self.color = colors[0]
        self.len = get_random_number_from_range(40, 50)
        self.direction = 0
        self.idx = self.len - 1

    def update(self):
        if self.direction == 0:  # trigo
            self.idx += 1
            if self.idx == NUM_PIXELS - 1:
                self.direction = 1
                self.idx = NUM_PIXELS - self.len
        else:  # anti-trigo
            self.idx -= 1
            if self.idx == 0:
                self.direction = 0
                self.idx = self.len - 1

    def light(self):
        pixels.fill(BLACK)
        pixels.show()
        for i in range(self.len):
            if self.direction == 1:
                simplified_idx = (self.idx + i) % NUM_PIXELS
            else:
                simplified_idx = (self.idx - i) % NUM_PIXELS
            pixels[simplified_idx] = self.color
        pixels.show()


if __name__ == "__main__":
    line = Line()
    while True:
        line.light()
        line.update()
        # time.sleep(0.01)
