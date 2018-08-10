#Importing libs

import sys, pygame
print(pygame.__version__)
import random

#We need to init PYGAME every time we use it

pygame.init()

#some default colors in RGB format (RED,GREEN,BLUE)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
col = (123,2,34)
pink = (255,200,200)

#Setting the size of our display(canvas)

size = width,height = 400,600
screen = pygame.display.set_mode(size)

#Class of  BIRD object(our flappy dot)

class Bird:

    #This is the constructor of this class.Every class needs one.
    def __init__(self,pos_X,pos_Y,r_m,velocity_m):
        self.posX = pos_X
        self.posY = pos_Y
        self.r = r_m
        self.velocity = velocity_m

    #Down here we'll find the object defs we're using

    #update_pos(self): Def for updating the BIRD position
    def update_pos(self):

        self.velocity += gravity
        self.posY += self.velocity
        if self.velocity < -lift:
            print("PREA MARE")
            self.velocity = -lift
            return
        if self.posY > 580:
            self.velocity = 0
            self.posY = 580
        if self.posY < self.r:
            self.velocity = 0
            self.posY = self.r

    def draw(self):
        pygame.draw.circle(screen,white,(self.posX,self.posY),self.r)

class Pipes:
    def __init__(self):
        self.abs_pos = random.randint(100,500)

        self.distance = 200
        self.thickness = 60

        self.up_x = self.distance
        self.up_y = 0
        self.up_width  = self.thickness
        self.up_height = self.abs_pos - 80

        self.down_x = self.distance
        self.down_y = self.abs_pos + 80
        self.down_width = self.thickness
        self.down_height = 520 - self.abs_pos
    def draw_abs_point(self):
        pygame.draw.circle(screen,white,(200,self.abs_pos),10)
    def update_pos_rand(self):
        self.abs_pos = random.randint(100,500)

        self.distance = 200
        self.thickness = 60

        self.up_x = self.distance
        self.up_y = 0
        self.up_width  = self.thickness
        self.up_height = self.abs_pos - 80

        self.down_x = self.distance
        self.down_y = self.abs_pos + 80
        self.down_width = self.thickness
        self.down_height = 520 - self.abs_pos
    def draw(self):
         pygame.draw.rect(screen,white,[self.up_x,self.up_y,self.up_width,self.up_height],2)
         pygame.draw.rect(screen,white,[self.down_x,self.down_y,self.down_width,self.down_height],2)


clock = pygame.time.Clock()

bird = Bird(50,50,20,0)
lift = 30
gravity = 1

pipe = Pipes()


#This is the MAIN LOOP.

while True:

    bird.update_pos()
    bird.draw()
    pipe.draw()
    pipe.draw_abs_point()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_SPACE:
                bird.velocity -= lift
                print(bird.velocity)
                print(bird.posY)
                print("SPACE")
            if event.key== pygame.K_r:
                pipe.update_pos_rand()


    pygame.display.update()
    pygame.display.flip()
    screen.fill(black)
    #pygame.time.delay(10)
    clock.tick(60)
