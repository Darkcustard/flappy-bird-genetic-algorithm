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

    birdy = 100
    birdyvel = 0

    running = True

    while running:


        window.fill((255,255,255))
        dt = clock.tick()/1000
        birdyvel += dt*1500
        birdy += birdyvel*dt

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

        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_SPACE]:
            birdyvel = -400

        pygame.draw.rect(window, (255,0,0), (100, birdy, 50, 50))

        pygame.display.update()






if __name__ == "__main__":
    main()
