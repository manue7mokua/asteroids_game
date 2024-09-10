import pygame 
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Initialize pygame
    pygame.init()

    # Set up game display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Clock for managing frame rate
    clock = pygame.time.Clock()
    
    # Create player object in center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Create required sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x, y)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    dt = 0

    running = True

    # Game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the player's state
        for obj in updatable:
            obj.update(dt)

        # Fill the display with black
        screen.fill((0, 0, 0))

        # Draw the player
        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()

        # Limit frames to 60 fps
        clock.tick(60)
        
        dt = clock.tick(60) / 1000

    # Close pygame
    pygame.quit()

if __name__ == "__main__":
    main()