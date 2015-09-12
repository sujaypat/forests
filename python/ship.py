import os
from random import random

import pygame

from buffalo import utils

class Ship:

    hit_sounds = [
        pygame.mixer.Sound(os.path.join('sounds','hit1.wav')),
        pygame.mixer.Sound(os.path.join('sounds','hit2.wav')),
    ]

    thruster_sound = pygame.mixer.Sound(os.path.join('sounds','thruster.wav'))

    thruster_channel = pygame.mixer.Channel(0)

    right_blasters = [
            pygame.image.load(os.path.join('images','rightblaster1.png')),
            pygame.image.load(os.path.join('images','rightblaster2.png')),
            pygame.image.load(os.path.join('images','rightblaster3.png')),
            pygame.image.load(os.path.join('images','rightblaster4.png')),
    ]
    left_blasters = [
            pygame.image.load(os.path.join('images','leftblaster1.png')),
            pygame.image.load(os.path.join('images','leftblaster4.png')),
    ]
    up_blasters = [
        pygame.image.load(os.path.join('images','upblaster1.png')),
        pygame.image.load(os.path.join('images','upblaster4.png')),
    ]
    down_blasters = [
        pygame.image.load(os.path.join('images','downblaster1.png')),
        pygame.image.load(os.path.join('images','downblaster4.png')),
    ]

    
    def __init__(self):
        Ship.thruster_sound.set_volume(0.25)
        self.pos = utils.SCREEN_M
        self.xv = 0
        self.yv = 0
        self.speed = 2
        self.hitstack = 0
        self.hp = 5
        self.surface = pygame.image.load(os.path.join('images','ship1.png'))
        self.hp_image = pygame.image.load(os.path.join('images', 'heart.png'))
        self.blaster_padding = 2
        self.rb_on = False
        self.lb_on = False
        self.ub_on = False
        self.db_on = False
        self.dead = False
        self.render_healthbar()

    def render_healthbar(self):
        if self.hp > 0:
            self.healthbar_surface = utils.empty_surface((32 * self.hp, 32))
            for i in range(self.hp):
                self.healthbar_surface.blit(self.hp_image, (32 * i, 0))
        else:
            self.healthbar_surface = utils.empty_surface((32, 32))    

    def update(self, paused):
        if paused:
            return
        self.hp -= self.hitstack
        if self.hitstack > 0:
            self.hitstack = 0
            self.render_healthbar()
        if not self.hp > 0:
            self.dead = True
        self.xv = 0
        self.yv = 0
        self.rb_on = False
        self.lb_on = False
        self.ub_on = False
        self.db_on = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.xv += self.speed
            self.rb_on = True
        if keys[pygame.K_a]:
            self.xv -= self.speed
            self.lb_on = True
        if keys[pygame.K_w]:
            self.yv -= self.speed
            self.ub_on = True
        if keys[pygame.K_s]:
            self.yv += self.speed
            self.db_on = True
        if keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_w] or keys[pygame.K_s]:
            if not Ship.thruster_channel.get_busy():
                Ship.thruster_channel.play(Ship.thruster_sound)
        else:
            Ship.thruster_channel.stop()
        x, y = self.pos
        x += self.xv
        y += self.yv
        self.pos = x, y
        return self.hitstack > 0

    def blit(self, dest):
        if not self.dead:
            dest.blit(self.surface, self.pos)
            if self.rb_on:
                dest.blit(
                    Ship.right_blasters[int(random() * len(Ship.right_blasters))],
                    (self.pos[0] - 32 - self.blaster_padding, self.pos[1]),
                )
            if self.lb_on:
                dest.blit(
                    Ship.left_blasters[int(random() * len(Ship.left_blasters))],
                    (self.pos[0] + 32 + self.blaster_padding, self.pos[1]),
                )
            if self.ub_on:
                dest.blit(
                    Ship.up_blasters[int(random() * len(Ship.up_blasters))],
                    (self.pos[0], self.pos[1] + 32 + self.blaster_padding),
                )
            if self.db_on:
                dest.blit(
                    Ship.down_blasters[int(random() * len(Ship.down_blasters))],
                    (self.pos[0], self.pos[1] - 32 - self.blaster_padding),
                )
        dest.blit(self.healthbar_surface, (5, utils.SCREEN_H - 5 - 32))
