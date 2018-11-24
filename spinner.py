import neopixel
import board
import time
import random


COLOR_MAX = 4

SPEED = 10

MUTATION_RATE = 0.05


def random_color():
    c = (0, 0, 0)
    while c == (0, 0, 0) or c == (COLOR_MAX, COLOR_MAX, COLOR_MAX):
        c = tuple(random.randint(0, COLOR_MAX) for i in range(3))
    return c


def invert(color):
    return tuple(COLOR_MAX - v for v in color)


def random_color_pair():
    c = random_color()
    return (c, invert(c))


def main():
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1.0, auto_write=False)
    pixels.fill((0, 0, 0))
    pixels.show()
    fg_color, bg_color = random_color_pair()

    n = len(pixels)
    i = 0
    j = int(n / 2)
    k = 1
    while True:
        if random.random() < MUTATION_RATE:
            fg_color, bg_color = random_color_pair()
        if random.random() < MUTATION_RATE:
            k = random.choice([1, -1])
        pixels[i] = fg_color
        pixels[(i + j)%n] = bg_color
        pixels.show()
        i = (i + k) % n
        time.sleep(1.0 / SPEED)


main()
