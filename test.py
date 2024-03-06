from nn.network import FeedForwardNetwork
from nn.visualization import visualize
from nn.config_parser import parse_config
import pygame


window = pygame.display.set_mode((1000,1000))
running = True

config = parse_config('config.txt')
network = FeedForwardNetwork([2,3,4,3,2], config)


while running:

    window.fill((50,50,50))
    visualize(window, network, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    pygame.display.update()