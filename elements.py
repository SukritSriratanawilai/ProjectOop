import pygame
from pygame.locals import *
import random
import time
from threading import Thread

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

    def catch():
        pass    

class Egg(object):
    def __init__(self, radius, color, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.radius = radius
        self.color = color

    def render(self, surface):
        pygame.draw.circle(surface, self.color, (self.x,self.y), self.radius, 0)

    def newPos():
        pass

class Bomb(object):
    def __init__(self, arg):
        super(Bomb, self).__init__()
        self.arg = arg

    def render():
        pass

    def newPos():
        pass
    
#class MyThread(Thread):
#    def __init__(self,player, surface):
#        Thread.__init__(self)
#        self.player = player
#        self.surface = surface
#    def run(self):
#        Player.render_position(self.player, self.surface)


