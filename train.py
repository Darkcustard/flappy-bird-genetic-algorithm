from nn import evolutionary


def evaluator( networks ):

    for network in networks:
        network.fitness += 1


population = evolutionary.Population([2,3,2],'config.txt')
population.fit( evaluator, 100 )