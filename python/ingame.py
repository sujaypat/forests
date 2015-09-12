import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button
from buffalo.input import Input
from buffalo.option import Option

from ship import Ship
from blasteroid import Blasteroid

class InGame(Scene):

    def __init__(self):
        super().__init__()
        self.BACKGROUND_COLOR = (25, 0, 75, 255)

        self.paused = True
        self.blasteroids = set(
            [Blasteroid(on_screen=True) for b in range(100)]
        )
        self.ship = Ship()

        self.labels.add(
            Label(
                (5, 5),
                "No Bloomberg Data Loaded -> Random Scatterplot",
            )
        )
        self.labels.add(
            Label(
                (5, 20),
                "Score:",
            )
        )

    def on_escape(self):
        del self.blasteroids
        utils.set_scene(Menu())

    def logic(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                utils.end = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.on_escape()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    self.paused = not self.paused
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.paused:
                    for button in self.buttons:
                        if button.get_rect().collidepoint( mouse_pos ):
                            button.set_selected(True)
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if self.paused:
                    for button in self.buttons:
                        button.set_selected(False)
                        if button.get_rect().collidepoint( mouse_pos ):
                            if button.func is not None:
                                button.func()

    def update(self):
        if not self.paused:
            for i in range(len(self.blasteroids)):
                blasteroid = self.blasteroids.pop()
                if blasteroid.update(self.ship):
                    self.blasteroids.add(blasteroid)        
        self.ship.update(self.paused)

    def blit(self):
        for blasteroid in self.blasteroids:
            blasteroid.blit(utils.screen)
        self.ship.blit(utils.screen)

from menu import Menu
