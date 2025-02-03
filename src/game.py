import pygame
from pygame.locals import QUIT
from config import BACKGROUND, FPS, WINDOW_WIDTH, WINDOW_HEIGHT
from pathlib import Path
import sys
from models.ball import Ball


def run():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Simple Ball", "Simple Ball")
    pygame.display.set_icon(pygame.image.load(Path(__file__).parent.parent / "assets" / "images" / "ball.png"))
    clock = pygame.time.Clock()

    # Load assets
    pygame.mixer.music.load(Path(__file__).parent.parent / "assets" / "audio" / "background.mp3")
    pygame.mixer.music.play(-1, 0)

    # Init variables
    ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

    while True:

        # Check for and handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Perform 'per frame' actions
        ball.update()

        # Clear the frame
        window.fill(BACKGROUND)

        # Draw frame elements
        ball.draw()

        # Update the frame
        pygame.display.update()

        # Lock FPS
        clock.tick(FPS)