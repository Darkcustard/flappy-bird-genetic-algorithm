import pygame
from src import environment


def main():

    window = pygame.display.set_mode(environment.resolution)
    clock = pygame.time.Clock()
    pipes = []
    pipes.append(environment.Pipe(1500,pipes))
    pipes.append(environment.Pipe(1900,pipes))
    pipes.append(environment.Pipe(2300,pipes))
    pipes.append(environment.Pipe(2700,pipes))

    running = True

    while running:


        window.fill((255,255,255))
        dt = clock.tick(120)/1000

        for pipe in pipes:
            pipe.draw(window)
            pipe.update(dt)

        for pipe in pipes:
            if pipe.x < -100:
                pipes.remove(pipe)
                pipes.append(environment.Pipe(1500, pipes))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        pygame.display.update()






if __name__ == "__main__":
    main()
