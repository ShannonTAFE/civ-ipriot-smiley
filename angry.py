from smiley import Smiley

import time

class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            if wide_open:
                eyes = self.WHITE
            else:
                eyes = self.complexion()
            self.pixels[pixel] = eyes

    def blink(self, delay=0.5):
        """
       Blinks the smiley's eyes once

        :param delay: Delay between blinks (in seconds)
        """

        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
