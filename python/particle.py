from random import random
import os

import pygame

from buffalo import utils

class Particle:

    surface = pygame.image.load(os.path.join('images', 'particle1.png'))
    
    def __init__(self, pos):
        self.pos = pos
        if random() > 0.5:
            xmod = -1
        else:
            xmod = 1
        if random() > 0.5:
            ymod = -1
        else:
            ymod = 1
        self.xv = xmod * (int(random() * 4) + 2)
        self.yv = ymod * (int(random() * 4) + 2)

    def update(self):
        x, y = self.pos
        x += self.xv
        y += self.yv
        self.pos = x, y

    def on_screen(self):
        x, y = self.pos
        return x > -8 and x < utils.SCREEN_W and y > -8 and y < utils.SCREEN_H

    def blit(self, dest):
        dest.blit(Particle.surface, self.pos)
