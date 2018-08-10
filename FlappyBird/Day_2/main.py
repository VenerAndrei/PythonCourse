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

        self.pipe_distance = 200
        self.pipe_thic = 60

        #UP PIPE POS
        self.up_pipe_y1 = self.abs_pos - 80
        self.up_pipe_x1 = self.pipe_distance + self.pipe_thic

        self.up_pipe_y2 = 0
        self.up_pipe_x2 = self.pipe_distance

        #DOWN PIPE POS
        self.down_pipe_y1 = self.abs_pos + 80
        self.down_pipe_x1 = self.pipe_distance + self.pipe_thic

        self.down_pipe_y2 = 600
        self.down_pipe_x2 = self.pipe_distance

        print("UP PIPE")
        print(self.up_pipe_x1,self.up_pipe_y1)
        print(self.up_pipe_x2,self.up_pipe_y2)
        print("verde",self.up_pipe_x2,self.up_pipe_y2)
        print("WHITE",self.up_pipe_x1,self.up_pipe_y1)

    def draw_abs_point(self):
        pygame.draw.circle(screen,white,(200,self.abs_pos),10)

    def update_pos_rand(self):
        self.abs_pos = random.randint(100,500)
    def draw(self):
        pygame.draw.circle(screen,white,(self.up_pipe_x1,self.up_pipe_y1),10)
        pygame.draw.circle(screen,green,(self.up_pipe_x2,self.up_pipe_y2),10)

        pygame.draw.circle(screen,red,(self.down_pipe_x1,self.down_pipe_y1),10)
        pygame.draw.circle(screen,blue,(self.down_pipe_x2,self.down_pipe_y2),10)

        pygame.draw.rect(screen,white,[200,0,288,260],2)
        pygame.draw.rect(screen,white,[self.up_pipe_x2,self.up_pipe_y2,self.up_pipe_x1,self.up_pipe_y1],2)
        pygame.draw.rect(screen,white,[self.down_pipe_x1,self.down_pipe_y1,self.down_pipe_x2,self.down_pipe_y2],2)
#Setting default vars/objects

clock = pygame.time.Clock()

bird = Bird(50,50,20,0)
lift = 30
gravity = 1

pipe = Pipes()


#This is the MAIN LOOP.

while True:

    bird.update_pos()
    bird.draw()

    pipe.draw_abs_point()
    pipe.draw()
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
