from pygame import image
from random import randint

# Create image cache
pipe_image = image.load('src/assets/pipe.png')
pipe_image.set_colorkey((255,255,255))

# Game Rules
resolution = (1400,650)



class Pipe:

    yrange = [-350, 0]
    xrange = [0, resolution[0]-100]
    image = pipe_image.copy()
    speed = 200

    def __init__(self, x, tracker_array):
        
        self.x = x
        self.y = randint(self.yrange[0], self.yrange[1])
        self.tracker_array = tracker_array

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def update(self, dt):
        self.x -= dt*self.speed


class Bird:

    pass



