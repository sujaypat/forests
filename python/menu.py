import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button
from buffalo.input import Input
from buffalo.option import Option

from blasteroid import Blasteroid

class Menu(Scene):

    def __init__(self):
        super().__init__()
        self.BACKGROUND_COLOR = (25, 0, 75, 255)
        self.NUM_BLASTEROIDS = 50
        self.bgblasteroids = set(
            [Blasteroid() for b in range(self.NUM_BLASTEROIDS)]
        )

        self.labels.add(
            Label(
                (5, 5),
                "Bloombasteroids v. 1.0",
            )
        )

        def go_to_in_game():
            del self.bgblasteroids
            utils.set_scene(InGame())
            
        self.buttons.add(
            Button(
                (utils.SCREEN_W / 2, utils.SCREEN_H / 2 + 60),
                "Play",
                func=go_to_in_game,
                x_centered=True,
                y_centered=True,
            )
        )

        self.buttons.add(
            Button(
                (utils.SCREEN_W / 2, utils.SCREEN_H / 2 + 120),
                "Exit",
                x_centered=True,
                y_centered=True,
                func=exit,
            )
        )

    def on_escape(self):
        exit()

    def update(self):
        for i in range(len(self.bgblasteroids)):
            blasteroid = self.bgblasteroids.pop()
            if blasteroid.update():
                self.bgblasteroids.add(blasteroid)
            else:
                self.bgblasteroids.add(Blasteroid())

    def blit(self):
        for blasteroid in self.bgblasteroids:
            blasteroid.blit(utils.screen)        

from ingame import InGame
