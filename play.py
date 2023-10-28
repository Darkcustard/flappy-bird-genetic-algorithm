import pygame
from src import environment
import sys
import random

def main():

    window = pygame.display.set_mode(environment.resolution)
    clock = pygame.time.Clock()
    pipes = []
    pipes.append(environment.Pipe(1500,pipes))
    pipes.append(environment.Pipe(1900,pipes))
    pipes.append(environment.Pipe(2300,pipes))
    pipes.append(environment.Pipe(2700,pipes))


    birds = []
    for x in range(1):
        bird = environment.Bird()
        bird.y = random.randint(0,600)
        birds.append(bird)

    running = True
 
    while running:

        
        window.fill((255,255,255))
        dt = clock.tick()/1000
        window.blit(environment.background_image, (0,0))

        for pipe in pipes:
            pipe.draw(window)
            pipe.update(dt)

            for bird in birds:
                if bird.check_collision_pipe(pipe):
                    birds.remove(bird)

        for pipe in pipes:
            if pipe.x < -100:
                pipes.remove(pipe)
                pipes.append(environment.Pipe(1500, pipes))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_SPACE]:
            for bird in birds:
                bird.jump()
        
        for bird in birds:
            bird.update(dt)
            bird.draw(window)


        pygame.display.update()






if __name__ == "__main__":
    main()
