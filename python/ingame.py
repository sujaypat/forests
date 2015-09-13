import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button
from buffalo.input import Input
from buffalo.option import Option

from ship import Ship
from blasteroid import Blasteroid
from bbmanager import BBManager

class InGame(Scene):

    def new_blasteroids(self):
        self.paused = True
        self.score += 1
        if hasattr(self, 'score_label'):
            self.labels.remove(self.score_label)
        self.score_label = Label(
            self.score_label_pos,
            str(self.score),
        )
        self.labels.add(self.score_label)
        try:
            self.name_value, self.ticker_name, self.data = BBManager.get_ticker_data()
            self.values = [eval(obj.Value) for obj in self.data]
            self.valmax = max(self.values)
            self.valmin = min(self.values)
            self.valrng = self.valmax - self.valmin
            def calcDateVal(s):
                return float(s[:4]) * 365 + float(s[5:7]) * 30 + float(s[8:])
            self.dates  = [calcDateVal(obj.Date) for obj in self.data]
            self.datmax = max(self.dates)
            self.datmin = min(self.dates)
            self.datrng = self.datmax - self.datmin
            self.dates  = [val - self.datmin for val in self.dates]
            self.values = [val - self.valmin for val in self.values]
            self.positions = [(int((date / self.datrng) * utils.SCREEN_W), int((val / self.valrng) * utils.SCREEN_H)) for date, val in zip(self.dates, self.values)]
            self.blasteroids = set(
                [Blasteroid(pos) for pos in self.positions]
            )
        except:
            self.ticker_name = "No Bloomberg Data Loaded -> Random Scatterplot"
            self.blasteroids = set(
                [Blasteroid(on_screen=True) for b in range(100)]
            )
        if hasattr(self, 'ticker_name_label'):
            self.labels.remove(self.ticker_name_label)
        self.ticker_name_label = Label(
            self.ticker_name_label_pos,
            self.ticker_name,
        )
        self.labels.add(self.ticker_name_label)
        self.name_value_big_label = Label(
            utils.SCREEN_M,
            self.name_value,
            font='default48',
            x_centered=True,
            y_centered=True,
        )
        self.labels.add(self.name_value_big_label)

    def __init__(self):
        super().__init__()
        self.BACKGROUND_COLOR = (25, 0, 75, 255)

        self.score = 0
        self.score_label_pos = 50, 20
        self.ticker_name_label_pos = 5, 5
        self.new_blasteroids()
        self.ship = Ship()
        
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
                    if not self.paused:
                        if self.name_value_big_label in self.labels:
                            self.labels.remove(self.name_value_big_label)
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
            if not self.ship.dead and not len(self.blasteroids) > 0:
                self.new_blasteroids()
        self.ship.update(self.paused)

    def blit(self):
        for blasteroid in self.blasteroids:
            blasteroid.blit(utils.screen)
        self.ship.blit(utils.screen)

from menu import Menu
