import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", (int(self.x), int(self.y)), self.radius, 2)

    def update(self, dt):
        # Move asteroid based on velocity and delta time
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt