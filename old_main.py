import pygame
import sys

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
FLOOR_Y = WINDOW_HEIGHT * 0.8
GRAVITY = 9.8
FLAP_POWER = -3.5
BIRD_MOVEMENT = 0
FPS = 120
OBSTACLE_SPEED = 2.0  # The speed at which the obstacle moves from right to left
GAP_SIZE = 200  # The size of the gap for the bird to pass through

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Set up font
font = pygame.font.Font(None, 36)  # Change the size as needed

bird_surface = pygame.image.load(
    'assets/bird.png').convert_alpha()  # load an image for the bird
bird_rect = bird_surface.get_rect(center=(50, WINDOW_HEIGHT/2))

upper_obstacle_rect = pygame.Rect(
    WINDOW_WIDTH, 0, 50, WINDOW_HEIGHT/2 - GAP_SIZE/2)
lower_obstacle_rect = pygame.Rect(
    WINDOW_WIDTH, WINDOW_HEIGHT/2 + GAP_SIZE/2, 50, WINDOW_HEIGHT)

game_active = True

while True:
    delta_time = clock.tick(FPS) / 1000  # Get delta time in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active:
                    BIRD_MOVEMENT = FLAP_POWER  # Bird flaps its wings
                else:
                    game_active = True
                    bird_rect.center = (50, WINDOW_HEIGHT/2)
                    upper_obstacle_rect.left = WINDOW_WIDTH
                    lower_obstacle_rect.left = WINDOW_WIDTH
                    BIRD_MOVEMENT = 0

    if game_active:
        BIRD_MOVEMENT += GRAVITY * delta_time  # Multiply by delta time
        bird_rect.centery += BIRD_MOVEMENT

        upper_obstacle_rect.x -= OBSTACLE_SPEED  # Move the upper obstacle to the left
        lower_obstacle_rect.x -= OBSTACLE_SPEED  # Move the lower obstacle to the left

        # If the obstacles have moved off the screen
        if upper_obstacle_rect.right < 0:
            upper_obstacle_rect.left = WINDOW_WIDTH  # Move it back to the right
            lower_obstacle_rect.left = WINDOW_WIDTH  # Move it back to the right

        # Check for collisions
        if bird_rect.colliderect(upper_obstacle_rect) or bird_rect.colliderect(lower_obstacle_rect):
            game_active = False

        screen.fill((0, 0, 0))  # fill the screen with black
        screen.blit(bird_surface, bird_rect)
        pygame.draw.rect(screen, (255, 0, 0), upper_obstacle_rect)
        pygame.draw.rect(screen, (255, 0, 0), lower_obstacle_rect)
    else:
        game_over_text = font.render("Game Over", True, pygame.Color('white'))
        screen.blit(game_over_text, (WINDOW_WIDTH/2 - game_over_text.get_width() /
                    2, WINDOW_HEIGHT/2 - game_over_text.get_height()/2))
        continue_text = font.render(
            "Press Space for a new game", True, pygame.Color('white'))
        screen.blit(continue_text, (WINDOW_WIDTH/2 - continue_text.get_width() /
                    2, WINDOW_HEIGHT/2 + continue_text.get_height()))

    # Draw FPS
    fps_text = font.render(str(int(clock.get_fps())),
                           True, pygame.Color('white'))
    screen.blit(fps_text, (WINDOW_WIDTH - fps_text.get_width(), 0))

    pygame.display.update()
