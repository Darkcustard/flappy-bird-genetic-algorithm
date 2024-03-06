from nn import evolutionary
from random import random, seed
from src import environment
import pygame

window = pygame.display.set_mode(environment.resolution)

def evaluator( networks ):

    #seed(7945)
    birds = []
    pipes = []
    pipes.append(environment.Pipe(500,pipes))
    pipes.append(environment.Pipe(900,pipes))
    pipes.append(environment.Pipe(1300,pipes))
    pipes.append(environment.Pipe(1700,pipes))

    clock = pygame.time.Clock()
    
    for x in range(len(networks)):
        birds.append(environment.Bird())

    birds_alive = len(networks)
    while birds_alive > 0:

        birds_alive = 0
        window.blit(environment.background_image, (0,0))
        dt = clock.tick() / 1000.0*2
        pygame.event.get()


        # Calculated closed pipes
        closepipes = [(pipe.x-environment.Bird.x, pipe) for pipe in pipes if pipe.x > 0]
        closepipes.sort(key=lambda x: x[0])
        closestpipe = closepipes[0][1]

        for i in range(len(networks)):

            network = networks[i]
            bird = birds[i]
            
            
            if bird.alive:
            
                birds_alive += 1

                inputs = [
                    bird.y / environment.resolution[1],
                    (closestpipe.y + 500 - (bird.y+25))/environment.resolution[1],
                    (closestpipe.x+50 - bird.x)/environment.resolution[0],
                    bird.yvel/bird.maxyvel,
                ]

                output = network.predict(inputs)
                if output[0] > 0.5:
                    bird.jump()






                bird.update(dt)
                bird.draw(window)
                
                network.fitness += dt

                # Bounds
                if bird.y < 0:
                    bird.alive = False
                if bird.y > environment.resolution[1]-50:
                    bird.alive = False

                # Check collisions
                for pipe in pipes:
                    if bird.check_collision_pipe(pipe):
                        network.fitness += 1/(abs(bird.y+25 - (500+pipe.y)))
                        bird.alive = False

            
        for pipe in pipes:
            pipe.update(dt)
            pipe.draw(window)

            if pipe.x < -100:
                pipes.remove(pipe)
                pipes.append(environment.Pipe(1500, pipes))

        pygame.display.update()





population = evolutionary.Population([4,1],'config.txt')
population.fit( evaluator, 1000 )
