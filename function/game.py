import pygame
from pygame.constants import QUIT, K_ESCAPE, KEYDOWN

import sys

def game(scr, k_d, k_w):

    # Initialize counters for the dragon and wolf
    counter_d = 0
    counter_w = 0

    # Initialize the timer
    timer = pygame.time.Clock()

    # Initialize the positions of the dragon and wolf
    pos_d = [300, 300]
    pos_w = [400, 600]

    # Initialize the speeds of the dragon and wolf
    sp_d = 0
    sp_w = 17

    # Initialize the index and count
    index = "wolf"
    count = 0

    # Main game loop
    while True:

        # Event handling
        for evt in pygame.event.get():
            if evt.type == QUIT or (evt.type == KEYDOWN and evt.key == K_ESCAPE):
                sys.exit()

        # Load and scale the background image
        background_image = pygame.image.load("images/background.jpg").convert()
        background_image = pygame.transform.scale(background_image, (scr.get_width(), scr.get_height()))
        scr.blit(background_image, (0, 0))

        # Move the wolf and dragon
        if index == "wolf":
            sp_w = 17
            sp_d = 0
            pos_w[0] += sp_w
            if abs(pos_w[0] - pos_d[0]) < k_w[0].get_width():
                count += 1
                if count == 2:
                    index = "dragon"
                    count = 0

        elif index == "dragon":
            sp_w = 0
            sp_d = 17
            pos_d[0] += sp_d
            if abs(pos_w[0] - pos_d[0]) < k_w[0].get_width():
                count += 1
                if count == 2:
                    index = "wolf"
                    count = 0

        # Keep the dragon and wolf within the screen
        if pos_d[0] > scr.get_width():
            pos_d[0] = -k_d[0].get_width()

        if pos_d[0] < -k_d[0].get_width():
            pos_d[0] = scr.get_width()

        if pos_w[0] > scr.get_width():
            pos_w[0] = -k_w[0].get_width()

        if pos_w[0] < -k_w[0].get_width():
            pos_w[0] = scr.get_width()

        # Draw the dragon and wolf
        scr.blit(k_d[counter_d], (pos_d[0], pos_d[1]))
        counter_d = (counter_d + 1) % len(k_d)

        scr.blit(k_w[counter_w], (pos_w[0], pos_w[1]))
        counter_w = (counter_w + 1) % len(k_w)

        # Update the display and set the frame rate
        pygame.display.update()
        timer.tick(7)