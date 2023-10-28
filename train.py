from nn import evolutionary
from random import random


def evaluator( networks ):

    for network in networks:
        network.fitness += random()


population = evolutionary.Population([2,3,2],'config.txt')
population.fit( evaluator, 100 )