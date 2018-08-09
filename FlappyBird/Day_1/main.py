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


#Setting default vars/objects

clock = pygame.time.Clock()
bird = Bird(50,50,20,0)
lift = 20
gravity = 1

#This is the MAIN LOOP.
while True:
    bird.update_pos()
    pygame.draw.circle(screen,white,(bird.posX,bird.posY),bird.r)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_SPACE:
                bird.velocity -= lift
                print(bird.velocity)
                print(bird.posY)
                print("SPACE")

    pygame.display.update()
    pygame.display.flip()
    screen.fill(black)
    #pygame.time.delay(10)
    clock.tick(60)
