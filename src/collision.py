import pygame


def check_collision(bird, obstacles):
    # Create a rectangle around the bird
    bird_rect = pygame.Rect(bird.x - 20, bird.y - 20, 40, 40)

    for obstacle in obstacles:
        if bird_rect.colliderect(obstacle.rect):
            return True  # Collision detected

    return False  # No collision detected
