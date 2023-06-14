import pygame
from input import handle_input
from objects import Bird, Obstacle
from collision import check_collision
from rendering import render_game_objects


class Game:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.bird = Bird(50, window_height // 2)  # Create the bird object
        self.obstacles = []  # List to store obstacle objects
        self.game_active = True

        # Add initial obstacles
        self.add_obstacle()

    def add_obstacle(self):
        gap_size = 200  # Gap size for the bird to pass through
        obstacle_width = 50
        obstacle_x = self.window_width
        # Adjust obstacle y-position based on time
        obstacle_y = pygame.time.get_ticks() / 4
        upper_obstacle = Obstacle(
            obstacle_x, obstacle_y, obstacle_width, gap_size, "upper")
        lower_obstacle = Obstacle(obstacle_x, obstacle_y + gap_size, obstacle_width,
                                  self.window_height - (obstacle_y + gap_size), "lower")
        self.obstacles.append(upper_obstacle)
        self.obstacles.append(lower_obstacle)

    def update(self, delta_time):
        if self.game_active:
            # Update bird position and velocity
            handle_input(self.bird)
            self.bird.update(delta_time)

            # Update obstacle positions
            for obstacle in self.obstacles:
                obstacle.update(delta_time)

            # Remove off-screen obstacles
            self.obstacles = [
                obstacle for obstacle in self.obstacles if obstacle.rect.right > 0]

            # Check for collisions
            if check_collision(self.bird, self.obstacles):
                self.game_active = False

            # Add new obstacles
            if self.obstacles[-1].rect.centerx < self.window_width // 2:
                self.add_obstacle()

    def render(self, screen):
        # Render game objects
        render_game_objects(screen, self.bird, self.obstacles)
