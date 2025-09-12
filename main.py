import pygame
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT)
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True
    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)

        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
