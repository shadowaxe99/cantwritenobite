import pygame
import sys
import json
from pygame.locals import *
sys.path.insert(0, '')
from pywritesmooth.pywritesmooth import Writer, get_stroke_path

pygame.init()

# Set up some constants
WIDTH = 600
HEIGHT = 400
FACTOR = 100
OFFSET_X = WIDTH // 2
OFFSET_Y = HEIGHT // 2

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Create the clock
clock = pygame.time.Clock()

# Load the data
with open('data.json', 'r') as f:
    data = json.load(f)

# Get the stroke path
stroke_path = get_stroke_path(data, FACTOR, OFFSET_X, OFFSET_Y)

# Create the writer
writer = Writer(stroke_path)

# Run until the user asks to quit
running = True
while running:
    # Fill the background
    window.fill((255, 255, 255))

    # Draw the writer
    writer.draw(window)

    # Flip the display
    pygame.display.flip()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Ensure we maintain a 30 frames per second rate
    clock.tick(30)

# Done! Time to quit.
pygame.quit()
