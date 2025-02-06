import pygame.image
from pygame import Surface
from pygame.event import Event
from pygame.locals import MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pathlib import Path


class Button:
    STATE_IDLE = 'idle'
    STATE_ARMED = 'armed'
    STATE_DISARMED = 'disarmed'

    def __init__(self, window: Surface, coordinates : tuple[int, int], up: Path, down: Path):
        self.window = window
        self.coordinates = coordinates
        self.surface_up = pygame.image.load(up)
        self.surface_down = pygame.image.load(down)
        self.collision = self.surface_up.get_rect()
        self.x = self.collision.x
        self.y = self.collision.y
        self.state = self.STATE_IDLE

    def handle_event(self, event : Event) -> bool:

        if event.type not in (MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP):
            return False

        event_point_in_button_collision = self.collision.collidepoint(event.pos)

        if self.state == Button.STATE_IDLE:
            if event.type == MOUSEBUTTONDOWN and event_point_in_button_collision:
                self.state = Button.STATE_ARMED

        elif self.state == Button.STATE_ARMED:
            if event.type == MOUSEBUTTONUP and event_point_in_button_collision:
                self.state = Button.STATE_IDLE
                return True

            if event.type == MOUSEMOTION and not event_point_in_button_collision:
                self.state = Button.STATE_DISARMED

        elif self.state == Button.STATE_DISARMED:
            if event_point_in_button_collision:
                self.state = Button.STATE_ARMED

            elif event.type == MOUSEBUTTONUP:
                self.state = Button.STATE_IDLE

        return False

    def draw(self):
        if self.state == Button.STATE_ARMED:
            self.window.blit(self.surface_down, self.coordinates)

        else:
            self.window.blit(self.surface_up, self.coordinates)
