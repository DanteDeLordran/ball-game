import random

import pygame.image
from pygame import Surface
from pathlib import Path


class Ball:

    def __init__(self, window : Surface , window_width : int, window_height : int):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.image = pygame.image.load(Path(__file__).parent.parent.parent / "assets" / "images" / "ball.png")
        self.fx = pygame.mixer.Sound(Path(__file__).parent.parent.parent / "assets" / "audio" / "boing.wav")
        self.collision = self.image.get_rect()
        self.width = self.collision.width
        self.height = self.collision.height
        self.max_width = self.window_width - self.width
        self.max_height = self.window_height - self.height
        self.x = random.randrange(0, self.max_width)
        self.y = random.randrange(0, self.max_height)
        speed_list = (-6, 6)
        self.x_speed = random.choice(speed_list)
        self.y_speed = random.choice(speed_list)

    def update(self):
        if (self.x < 0) or (self.x > self.max_width + 1):
            self.x_speed = -self.x_speed
            self.fx.play()

        if (self.y < 0) or (self.y > self.max_height + 1):
            self.y_speed = -self.y_speed
            self.fx.play()

        self.x += self.x_speed
        self.y += self.y_speed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))