import time
import board
import neopixel
from leds.config.colors import BLACK, RED, GREEN, BLUE, WHITE, PURPLE, PINK, ORANGE, CYAN, MAGENTA
from leds.config.positions import WALL, SHELF, EDGE, TOP
from leds.utils import fill_list, get_random_element_from_list, get_random_number_from_range


pixel_pin = board.D18

num_pixels = 223

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

colors = {
    idx: color for idx, color in enumerate([RED, GREEN, BLUE, PURPLE, PINK, ORANGE, CYAN, MAGENTA])
}
color_indices = list(range(len(colors)))


class Line:
    def __init__(self):
        self.color_idx = 0
        self.len = get_random_number_from_range(5, 10)

    def update(self, idx: int):
        if idx % num_pixels == 0:
            color_idx = get_random_element_from_list(color_indices, self.color_idx)
            self.color_idx = color_idx

    def light(self, idx: int):
        pixels.fill(BLACK)
        pixels.show()
        for i in range(self.len):
            pixels[(idx - i) % num_pixels] = colors[self.color_idx]
        pixels.show()


if __name__ == "__main__":
    idx = 0
    line = Line()
    while True:
        line.light(idx)
        idx += 1
        line.update(idx)
