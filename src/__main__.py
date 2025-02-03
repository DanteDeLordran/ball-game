import random

import pygame
from pygame.locals import QUIT
import sys
from pathlib import Path

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 15
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3

def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    ball = pygame.image.load(Path(__file__).parent.parent / "assets" / "images" / "ball.png")
    target = pygame.image.load(Path(__file__).parent.parent / "assets" / "images" / "target.jpg")

    ball_x = random.randrange(MAX_WIDTH)
    ball_y = random.randrange(MAX_HEIGHT)

    target_rect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ball_x -= N_PIXELS_TO_MOVE
                elif event.key == pygame.K_RIGHT:
                    ball_x += N_PIXELS_TO_MOVE
                elif event.key == pygame.K_UP:
                    ball_y -= N_PIXELS_TO_MOVE
                elif event.key == pygame.K_DOWN:
                    ball_y += N_PIXELS_TO_MOVE

        ball_rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

        if ball_rect.colliderect(target_rect):
            print("Target collides with ball")

        window.fill(BLACK)

        window.blit(target, (TARGET_X, TARGET_Y))
        window.blit(ball, (ball_x, ball_y))

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
