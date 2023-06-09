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
        self.color_idx = 0
        self.previous_color_idx = 0
        self.len = get_random_number_from_range(10, 15)

    def update(self, idx: int):
        if idx % NUM_PIXELS == 0:
            color_idx = get_random_element_from_list(color_indices, self.color_idx)
            self.previous_color_idx = self.color_idx
            self.color_idx = color_idx

    def light(self, idx: int):
        pixels.fill(BLACK)
        pixels.show()
        for i in range(self.len):
            simplified_idx = (idx - i) % NUM_PIXELS
            if (simplified_idx > NUM_PIXELS - self.len) and (idx % NUM_PIXELS) < self.len:
                color = colors[self.previous_color_idx]
            else:
                color = colors[self.color_idx]
            color = apply_brightness(color, 1 - (i / (self.len + 4)))
            pixels[simplified_idx] = color
        pixels.show()


if __name__ == "__main__":
    idx = 0
    line = Line()
    while True:
        line.light(idx)
        idx += 1
        line.update(idx)
