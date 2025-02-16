import sys
from pathlib import Path

import pygame
from pygame.locals import QUIT

from config import BACKGROUND, FPS, WINDOW_WIDTH, WINDOW_HEIGHT
from models.ball import Ball
from models.button import Button
from models.text import Text


def run(num_balls=1):  # Default to 50 balls if not provided
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Simple Ball", "Simple Ball")
    pygame.display.set_icon(pygame.image.load(Path(__file__).parent.parent / "assets" / "images" / "ball.png"))
    clock = pygame.time.Clock()

    # Load assets
    pygame.mixer.music.load(Path(__file__).parent.parent / "assets" / "audio" / "background.mp3")
    pygame.mixer.music.play(-1, 0)

    # Init variables
    balls: list[Ball] = []
    for _ in range(num_balls):  # Use the num_balls parameter
        balls.append(Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT))

    restart_button = Button(window, (280,60), Path(__file__).parent.parent / "assets" / "images" / "button_up.png", Path(__file__).parent.parent / "assets" / "images" / "button_down.png")
    frame_count_label = Text(window, (60,20), 'Loops', (255,255,255))
    frame_count_display = Text(window, (500,20), '', (255,255,255))
    frame_counter = 0

    while True:
        # Check for and handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if restart_button.handle_event(event):
                frame_counter = 0

        # Perform 'per frame' actions
        for ball in balls:
            ball.update()
        frame_counter += 1
        frame_count_display.set_value(str(frame_counter))

        # Clear the frame
        window.fill(BACKGROUND)

        # Draw frame elements
        restart_button.draw()
        for ball in balls:
            ball.draw()
        frame_count_label.draw()
        frame_count_display.draw()

        # Update the frame
        pygame.display.update()

        # Lock FPS
        clock.tick(FPS)