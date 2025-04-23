import pygame

def my_animation(w1, h1, name, animation_frames):

    # Load the sprite image
    sprite = pygame.image.load("{0}.png".format(name)).convert_alpha()


    # Get the width and height of the sprite image
    width, height = sprite.get_size()

    # Calculate the width and height of each frame
    w, h = width / w1, height / h1

    # Initialize the row variable
    row = 0

    # Loop through each frame and append it to the animation_frames list
    for j in range(h1):
        for i in range(w1):
            animation_frames.append(sprite.subsurface(pygame.Rect(i * w, row, w, h)))
            
        # Increment the row variable
        row += h