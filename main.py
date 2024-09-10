import pygame 
from player import Player

from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()

    # Set up game display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create player object in center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Clock for managing frame rate
    clock = pygame.time.Clock()
    dt = 0

    running = True

    # Game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the player's state
        player.update(dt)

        # Fill the display with black
        screen.fill((0, 0, 0))

        # Draw the player
        player.draw(screen)

        # Update the display
        pygame.display.flip()

        # Limit frames to 60 fps
        clock.tick(60)
        
        dt = clock.tick(60) / 1000

    # Close pygame
    pygame.quit()

if __name__ == "__main__":
    main()