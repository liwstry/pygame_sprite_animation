import pygame

from function.my_animation import my_animation
from function.game import game

def main():

    # Initialize the pygame module
    pygame.init()

    # Set the screen size to 800x800 pixels
    scr = pygame.display.set_mode((800, 800), 0, 32)

    # Create empty lists to store the dragon and wolf images
    kd = []
    kw = []

    # Call the my_animation function to load the dragon images and store them in the kd list
    my_animation(5, 1, "images/dragon", kd)
    # Call the my_animation function to load the wolf images and store them in the kw list
    my_animation(6, 1, "images/wolf", kw)

    # Call the game function to start the game
    game(scr, kd, kw)

if __name__ == "__main__":
    main()