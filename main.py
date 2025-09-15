import pygame

from constants import (SCREEN_WIDTH, SCREEN_HEIGHT)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                pygame.quit()
                raise SystemExit
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()

        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
