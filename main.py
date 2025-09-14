import pygame
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT)
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
