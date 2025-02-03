import random

import pygame
from pygame import Rect
from pygame.locals import QUIT
import sys
from pathlib import Path

# Defining pygame constants

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 6

def main():

    # Init game

    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    # Load assets

    ball = pygame.image.load(Path(__file__).parent.parent / "assets" / "images" / "ball.png")
    target = pygame.image.load(Path(__file__).parent.parent / "assets" / "images" / "target.jpg")

    # Init variables

    ball_x = random.randrange(MAX_WIDTH)
    ball_y = random.randrange(MAX_HEIGHT)
    target_rect = Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

    while True:

        # Check for and handle events

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Perform 'per frame' actions

        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_LEFT]:
            ball_x -= N_PIXELS_TO_MOVE

        if key_pressed[pygame.K_RIGHT]:
            ball_x += N_PIXELS_TO_MOVE

        if key_pressed[pygame.K_UP]:
            ball_y -= N_PIXELS_TO_MOVE

        if key_pressed[pygame.K_DOWN]:
            ball_y += N_PIXELS_TO_MOVE

        ball_rect = Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

        if ball_rect.colliderect(target_rect):
            print("Target collides with ball")

        # Clear the frame

        window.fill(BLACK)

        # Draw frame elements

        window.blit(target, (TARGET_X, TARGET_Y))
        window.blit(ball, (ball_x, ball_y))

        # Update the frame

        pygame.display.update()

        # Lock FPS

        clock.tick(FPS)


if __name__ == "__main__":
    main()
