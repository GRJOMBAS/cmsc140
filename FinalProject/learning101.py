import pygame

pygame.init()

from pygame.locals import (
    QUIT
)

RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

screenHeight = 720
screenWidth = 1080
screen = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption("Game 101")


rectWidth = 30
rectHeight = 150
first_rect = pygame.Rect(
    (screenWidth - rectWidth)/2, # left
    (3*(screenHeight-rectHeight))/4, # top
    rectWidth,  # width
    rectHeight  # height
  )

pygame.draw.rect(screen, BLUE, first_rect)

pygame.display.flip() # refresh the screen

pygame.draw.line(
    screen,     # where to draw the line
    WHITE,      # line color
    [0, 0],     # x,y start point
    [100, 100], # x,y end point
    5           # line width
  )

ellipse_rect = pygame.Rect(
    400, # left
    400, # top
    40,  # width
    80   # height
  )
pygame.draw.ellipse(
  screen,       # where to draw ellipse
  RED,          # color
  ellipse_rect  # rectangle to draw inside
)
pygame.display.flip() # refresh the screen

pygame.draw.polygon(
    screen,                     # where to draw the polygon
    RED,                        # color
    [[0,0], [200,200], [100,0]] # x,y coordinates of vertices
  )
pygame.display.flip() # refresh the screen

running = True
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user click the window close button? If so, stop the loop.
        if event.type == QUIT:
            running = False