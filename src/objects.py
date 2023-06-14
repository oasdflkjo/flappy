import pygame


class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.gravity = 0.6

    def flap(self):
        self.velocity = -9

    def update(self, delta_time):
        self.velocity += self.gravity * delta_time
        self.y += self.velocity * delta_time


class Obstacle:
    def __init__(self, x, y, width, height, obstacle_type):
        self.rect = pygame.Rect(x, y, width, height)
        self.obstacle_type = obstacle_type

    def update(self, delta_time):
        self.rect.x -= 2
