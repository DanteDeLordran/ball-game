import random

import pygame
from pygame import Rect
from pygame.locals import QUIT
import sys
from pathlib import Path

# Defining pygame constants

BACKGROUND = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 30
N_PIXELS_TO_MOVE = 6

def main():
    global BACKGROUND
    # Init game

    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Simple Ball", "Simple Ball")
    pygame.display.set_icon(pygame.image.load(Path(__file__).parent.parent / "assets" / "images" / "ball.png"))
    clock = pygame.time.Clock()

    # Load assets

    ball = pygame.image.load(Path(__file__).parent.parent / "assets" / "images" / "ball.png")

    # Init variables

    ball_rect = ball.get_rect()
    max_width = WINDOW_WIDTH - ball_rect.width
    max_height = WINDOW_HEIGHT - ball_rect.height
    ball_rect.x = random.randrange(max_width)
    ball_rect.y = random.randrange(max_height)
    x_speed = N_PIXELS_TO_MOVE
    y_speed = N_PIXELS_TO_MOVE

    while True:

        # Check for and handle events

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Perform 'per frame' actions

        if (ball_rect.x < 0) or (ball_rect.x > max_width + 1):
            x_speed = -x_speed
            BACKGROUND = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if (ball_rect.y < 0) or (ball_rect.y > max_height + 1):
            y_speed = -y_speed
            BACKGROUND = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        ball_rect.x += x_speed
        ball_rect.y += y_speed

        # Clear the frame

        window.fill(BACKGROUND)

        # Draw frame elements

        window.blit(ball, ball_rect)

        # Update the frame

        pygame.display.update()

        # Lock FPS

        clock.tick(FPS)


if __name__ == "__main__":
    main()
