import pygame
from src import environment
import sys

def main():

    window = pygame.display.set_mode(environment.resolution)
    clock = pygame.time.Clock()
    pipes = []
    pipes.append(environment.Pipe(1500,pipes))
    pipes.append(environment.Pipe(1900,pipes))
    pipes.append(environment.Pipe(2300,pipes))
    pipes.append(environment.Pipe(2700,pipes))
    bird = environment.Bird()

    running = True

    while running:

        
        window.fill((255,255,255))
        window.blit(environment.background_image, (0,0)) 
        dt = clock.tick()/1000

        for pipe in pipes:
            pipe.draw(window)
            pipe.update(dt)
            if bird.check_collision_pipe(pipe):
                sys.exit()

        for pipe in pipes:
            if pipe.x < -100:
                pipes.remove(pipe)
                pipes.append(environment.Pipe(1500, pipes))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_SPACE]:
            bird.jump()
        
        bird.update(dt)
        bird.draw(window)


        pygame.display.update()






if __name__ == "__main__":
    main()
