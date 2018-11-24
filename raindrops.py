import neopixel
import board
import time
import random


SPEED = 10

MUTATION_RATE = 0.05

MAX_BRIGHTNESS = 10


class Fader(object):
    """\
    A Fader is a light that gradually changes from color to another.

    A Fader has a Color, a Target Color, and a Speed.

    The Color is the color of the light. Color is an RGB tuple.

    The Target Color is the color to fade to. Target Color is an RGB tuple.

    The Speed is how fast the light transitions to the target
    color. (1 <= speed <= 3)

    """

    def __init__(self, color=(0, 0, 0), speed=0):
        self.color = color
        self.target_color = color
        self.speed = speed or random_speed()

    def switch(self, color=None, speed=0):
        self.target_color = color or random_color()
        self.speed = speed or random_speed()

    def auto_switch(self):
        x = random.random()
        if x < 0.4:
            self.switch((0, 0, 0))
        elif x < 0.8:
            self.switch()
        self.speed = random.randint(1, 3)

    def _transition(self, v1, v2):
        if v1 < v2:
            v1 = min(v1 + self.speed, v2)
        elif v1 > v2:
            v1 = max(v1 - self.speed, v2)
        return v1

    def fade(self):
        self.color = tuple(
            self._transition(v1, v2)
            for (v1, v2) in zip(self.color, self.target_color)
        )

    def is_fading(self):
        return self.color != self.target_color


def shuffle(l):
    result = []
    while len(l) > 1:
        e = random.choice(l)
        l.remove(e)
        result.append(e)
    result.append(l[0])
    return result


def random_color():
    # Create a brightness budget
    x = random.randint(0, MAX_BRIGHTNESS * 3)
    # Carve out 3 random values from the budget
    v1 = random.randint(0, x)
    v2 = random.randint(0, x - v1)
    v3 = x - v1 - v2
    # Shuffle the values
    c = shuffle([v1, v2, v3])
    return tuple(c)


def random_speed():
    lower = max(1, int(MAX_BRIGHTNESS / 4))
    upper = max(1, int(MAX_BRIGHTNESS / 2))
    return random.randint(lower, upper)


def main():
    pixels = neopixel.NeoPixel(
        board.NEOPIXEL, 10, brightness=1.0, auto_write=False)
    pixels.fill((0, 0, 0))
    pixels.show()
    faders = [Fader() for p in pixels]

    n = len(pixels)
    while True:
        for i in range(n):
            f = faders[i]
            if f.is_fading():
                f.fade()
            else:
                f.auto_switch()
            pixels[i] = f.color
        pixels.show()
        time.sleep(1.0 / SPEED)


main()
