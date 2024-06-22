import pygame
import sys

pygame.init()

# Set up the display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rotating Surface Example')

# Create a surface (a green square in this example)
square_size = 100
surface = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
surface.fill((0, 255, 0))  # Green color

# Get the rectangle (Rect object) of the surface
rect = surface.get_rect(center=(width // 2, height // 2))

angle = 0
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))  # White background

    # Rotate the surface
    rotated_surface = pygame.transform.rotate(surface, angle)
    rotated_rect = rotated_surface.get_rect(center=rect.center)

    # Blit the rotated surface onto the screen
    screen.blit(rotated_surface, rotated_rect)

    # Update the angle for the next frame
    angle += 1
    if angle >= 360:
        angle = 0

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()