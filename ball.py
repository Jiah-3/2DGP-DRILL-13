from pico2d import load_image, draw_rectangle

import common
from random import randint

sx = 0
sy = 0

class Ball:
    def __init__(self):

        self.x, self.y = randint(50, common.court.w - 50), randint(50, common.court.h - 50)
        self.image = load_image('ball21x21.png')

    def update(self):
        pass


    def handle_event(self, event):
        pass


    def draw(self):
        global sx, sy
        sx = self.x - common.court.window_left
        sy = self.y - common.court.window_bottom
        self.image.draw(sx, sy)
        draw_rectangle(*self.get_bb())

    # fill here
    def get_bb(self):
        return sx - 10, sy - 10, sx + 10, sy + 10

    def handle_collision(self, group, other):
        pass