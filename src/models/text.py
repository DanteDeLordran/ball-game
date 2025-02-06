import pygame
from pygame import Surface


class Text:

    def __init__(self, window : Surface, coordinates : tuple[int,int], value : str, color : tuple[int,int,int]):
        pygame.font.init()
        self.window = window
        self.coordinates = coordinates
        self.font = pygame.font.SysFont(None, 30)
        self.color = color
        self.text = None
        self.set_value(value)

    def set_value(self, value):
        if self.text == value:
            return

        self.text = value
        self.text_surface = self.font.render(self.text, True, self.color)

    def draw(self):
        self.window.blit(self.text_surface, self.coordinates)