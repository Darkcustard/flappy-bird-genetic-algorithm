from pygame import image
from random import randint
from pygame import transform

# Create image cache
pipe_image = image.load('src/assets/pipe.png')
pipe_image.set_colorkey((255,255,255))

bird_image = image.load('src/assets/bird.png')
bird_image.set_colorkey((255,255,255))

background_image = image.load('src/assets/background.jpg')
background_image = transform.scale(background_image, (1400, 650))

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

    g = 1000
    maxyvel = 500
    jumpforce = 400
    x = 100
    y = 300
    yvel = 0
    rotfactor = 20

    def __init__(self):
        self.image = bird_image.copy()
    
    def draw(self,window):
        angle = self.yvel/self.maxyvel*-self.rotfactor
        rotated_copy = transform.rotate(self.image, angle)
        window.blit(rotated_copy,  (self.x, self.y))

    def check_collision_pipe(self, pipe : Pipe ):
        
        x,y = (pipe.x-self.x, pipe.y-self.y)

        if x < 50 and x > -100:
            if y > -400 or y < -550:
                return True
            
        return False




    def jump(self):
        self.yvel = -self.jumpforce

    def update(self, dt):

        self.yvel += self.g*dt

        # Enforce Max velocity
        if abs(self.yvel) > self.maxyvel:
            self.yvel /= abs(self.yvel)
            self.yvel *= self.maxyvel
        
        self.y += self.yvel*dt




