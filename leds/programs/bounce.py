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
from typing import Tuple


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
    def __init__(self, initial_sum: int = 0):
        self.color = colors[get_random_element_from_list(color_indices, 0)]
        self.len = get_random_number_from_range(10, 15)
        self.direction = 0
        self.idx = self.len - 1 + initial_sum
        self.next_idx = self.idx + 1
        self.next_direction = self.direction

    def update(self):
        def _get_next_idx_direction(idx: int, direction: int) -> Tuple[int, int]:
            if direction == 0:  # trigo
                idx += 1
                if idx == NUM_PIXELS - 1:
                    direction = 1
                    idx = NUM_PIXELS - self.len
            else:  # anti-trigo
                idx -= 1
                if idx == 0:
                    direction = 0
                    idx = self.len - 1
            return idx, direction

        self.idx, self.direction = _get_next_idx_direction(self.idx, self.direction)
        self.next_idx, self.next_direction = _get_next_idx_direction(self.idx, self.direction)

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
    lines = []
    line1 = Line(initial_sum=0)
    line2 = Line(initial_sum=100)
    lines = [line1, line2]
    while True:
        # time.sleep(0.01)
        trigos = [line for line in lines if line.direction == 0]
        anti_trigos = [line for line in lines if line.direction == 1]
        for trigo in trigos:
            for anti_trigo in anti_trigos:
                if abs(trigo.next_idx - anti_trigo.next_idx) <= 1:
                    trigo.idx = trigo.idx - (trigo.len - 1)
                    trigo.direction = 1
                    anti_trigo.idx = anti_trigo.idx + (anti_trigo.len - 1)
                    anti_trigo.direction = 0

        for line in lines:
            line.light()
            line.update()
