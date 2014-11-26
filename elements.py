import pygame
from pygame.locals import *
import random
import time
from threading import Thread
#random.randint(1, 10)  # Integer from 1 to 10, endpoints included

class Player(object):
    
    def __init__(self, pos, color, width = 25, speed = (2.5,0)):
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.width = width
        self.vx = speed[0]
        self.vy = speed[1]

    def render(self, surface):
        #MyThread(self, surface).start()
        #time.sleep(1)
        pygame.draw.rect(surface,self.color,(self.x,self.y,25,25))

    #def render_position(self,surface):
    #    pygame.draw.rect(surface,self.color,(self.x,self.y,25,25))

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def setSpeed(self, x, y):
        self.vx = x
        self.vy = y

    def catch_egg(self, Egg):
        return (self.x - self.width/2.0) < Egg.x < (self.x + self.width) and (self.y - self.width/2.0) < Egg.y < (self.y + self.width)

    def catch_bomb(self, Bomb):
        return (self.x - self.width/2.0) < Bomb.x < (self.x + self.width) and (self.y - self.width/2.0) < Bomb.y < (self.y + self.width)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Body(object):
    def __init__(self,color):
        self.x = 25
        self.y = 25
        self.color = color

    def render(self, surface):   
        pygame.draw.rect(surface,self.color,(self.x,self.y,25,25))    

    def update(self,x,y):
        self.x = x
        self.y = y

class Egg(object):
    def __init__(self, radius, color, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.radius = radius
        self.color = color

    def render(self, surface):
        pygame.draw.circle(surface, self.color, (self.x,self.y), self.radius, 0)

    def newPos(self,x,y):
        self.x = random.randint(25,x)
        self.y = random.randint(25,y)

class Bomb(object):
    def __init__(self, radius, color, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.radius = radius
        self.color = color

    def render(self, surface):
        pygame.draw.circle(surface, self.color, (self.x,self.y), self.radius, 0)

    def newPos(self,x,y):
        self.x = random.randint(25,x)
        self.y = random.randint(25,y)
