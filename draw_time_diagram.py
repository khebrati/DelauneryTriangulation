import pygame
import json

# Load data from JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

# Convert keys and values to integers
data = {int(k): float(v) * 1000 for k, v in data.items()}

# Pygame setup
pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Coordinate Plane")
clock = pygame.time.Clock()

# Coordinate plane setup
origin = (window_size[0] // 2, window_size[1] // 2)
scale = 0.5  # Change this to scale the points

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the coordinate plane
    pygame.draw.line(screen, (0, 0, 0), (0, origin[1]), (window_size[0], origin[1]))  # x-axis
    pygame.draw.line(screen, (0, 0, 0), (origin[0], 0), (origin[0], window_size[1]))  # y-axis

    # Plot the points and connect them with lines
    points = sorted(data.items())  # Sort the points by x-coordinate
    for i in range(len(points) - 1):
        pygame.draw.circle(screen, (255, 0, 0), (origin[0] + points[i][0] * scale, origin[1] - points[i][1] * scale), 5)
        pygame.draw.line(screen, (0, 0, 255), (origin[0] + points[i][0] * scale, origin[1] - points[i][1] * scale), (origin[0] + points[i+1][0] * scale, origin[1] - points[i+1][1] * scale))

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()