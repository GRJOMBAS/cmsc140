# Import the pygame module
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_LEFT,
    K_DOWN,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

# Define constants for the screen width and height
screenWidth = 1080
screenHeight = 720

# Create the screen object
# The size is determined by the constant screenWidth and screenHeight
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Fill the screen with white
screen.fill((255, 255, 0))
pygame.display.flip()

# Create a surface and pass in a tuple containing its length and width
radius = 75
surf = pygame.draw.circle(screen, (0, 0, 0), ((screenWidth-radius)/4, (screenHeight-radius)/4), radius)
pygame.display.flip()

pygame.draw.polygon(
    screen,                     # where to draw the polygon
    [0,0,0],                        # color
    [[screenWidth/2,screenHeight/2], [screenWidth,screenHeight], [screenWidth,0]] # x,y coordinates of vertices
  )
pygame.display.flip() # refresh the screen

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

