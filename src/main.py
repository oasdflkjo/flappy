import pygame
from game import Game

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Create an instance of the game
game = Game(WINDOW_WIDTH, WINDOW_HEIGHT)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    delta_time = clock.tick(60) / 1000  # Get delta time in seconds

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game state
    game.update(delta_time)

    # Render the game
    screen.fill((0, 0, 0))  # Fill the screen with black
    game.render(screen)
    pygame.display.update()

# Quit the game
pygame.quit()
