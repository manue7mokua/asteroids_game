import pygame 
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initialize pygame
    pygame.init()

    # Set up game display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Clock for managing frame rate
    clock = pygame.time.Clock()
    
    # Create player object in center of the screen
    x_starting_position = SCREEN_WIDTH / 2
    y_starting_position = SCREEN_HEIGHT / 2

    # Create required sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player_shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (player_shots, updatable, drawable)
    asteroid_field = AsteroidField()

    player = Player(x_starting_position, y_starting_position)

    dt = 0

    running = True

    # Game loop
    while running:
        # Limit frames to 60 fps
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the player's state
        for obj in updatable:
            obj.update(dt)


        # Check for collision between player and asteroids
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print(f"Player {player} just got hit by an asteroid {asteroid}.")
                print("GAME OVER MATE!")
                sys.exit()

            for shot in player_shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.kill()

        # Fill the display with black
        screen.fill("black")

        # Draw the player
        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()

    # Close pygame
    pygame.quit()

if __name__ == "__main__":
    main()