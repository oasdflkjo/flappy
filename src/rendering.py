import pygame


def render_game_objects(screen, bird, obstacles):
    # Render the bird
    pygame.draw.circle(screen, (255, 255, 0), (int(bird.x), int(bird.y)), 20)

    # Render the obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), obstacle.rect)
