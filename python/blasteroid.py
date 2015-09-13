import os
from random import random

import pygame

from buffalo import utils

from ship import Ship
from particle import Particle

class Blasteroid:

    surfaces = [
        pygame.image.load(os.path.join('images','asteroid1.png')),
        pygame.image.load(os.path.join('images','asteroid2.png')),
        pygame.image.load(os.path.join('images','asteroid3.png')),
        pygame.image.load(os.path.join('images','asteroid4.png')),
    ]
    
    def __init__(self, pos=None, on_screen=False):
        """
        on_screen will set self.pos to a random position on the screen
        if and only if self.pos is not specified as well.
        If self.pos is specified, on_screen will have no effect.
        """
        if pos is None:
            if on_screen:
                self.pos = int(random() * utils.SCREEN_W), int(random() * utils.SCREEN_H)
            else:
                xside = random() > 0.5
                yside = random() > 0.5
                if random() > 0.5:
                    x = xside * (utils.SCREEN_W + 64) - 32
                    y = int(utils.SCREEN_H * random())
                else:
                    x = int(utils.SCREEN_W * random())
                    y = yside * (utils.SCREEN_H + 64) - 32
                self.pos = x, y
        else:
            self.pos = pos
        possibilities = len(Blasteroid.surfaces)
        n = int(random() * possibilities)
        self.surface = Blasteroid.surfaces[n]
        if random() > 0.5:
            xmod = -1
        else:
            xmod = 1
        if random() > 0.5:
            ymod = -1
        else:
            ymod = 1
        self.xv, self.yv = 0, 0
        while (self.xv == 0 and self.yv == 0) or (self.xv ** 2 + self.yv ** 2) ** 0.5 < 5:
            self.xv = xmod * int(random() * 5)
            self.yv = ymod * int(random() * 5)
        self.particles = set()
        self.dead = False

    def are_all_particles_on_screen(self):
        if not self.dead:
            return True
        else:
            for particle in self.particles:
                if particle.on_screen():
                    return True
        return False

    def update(self, ship=None):
        if not self.dead:
            x, y = self.pos
            x += self.xv
            y += self.yv
            self.pos = x, y
            if ship is not None and utils.dist(ship.pos, self.pos) < 32:
                ship.hitstack += 1
                possibilities = len(Ship.hit_sounds)
                n = int(random() * possibilities)
                open_channel = pygame.mixer.find_channel()
                open_channel.queue(Ship.hit_sounds[n])
                self.dead = True
                self.particles = set(
                    [Particle(self.pos) for p in range(int(random() * 10) + 1)]
                )
            return x > -32 and x < utils.SCREEN_W + 32 and y > -32 and y < utils.SCREEN_H + 32
        else:
            for particle in self.particles:
                particle.update()
            
        return self.are_all_particles_on_screen()

    def blit(self, dest):
        if not self.dead:
            dest.blit(self.surface, self.pos)
        else:
            for particle in self.particles:
                particle.blit(utils.screen)
