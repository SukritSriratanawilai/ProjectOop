import pygame
from pygame.locals import *
from gamelib import SimpleGame
from elements import *
import random

class SnakeGame(SimpleGame):
    
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    YELLOW = pygame.Color('yellow')
    RED = pygame.Color('red')
    V = 25
    def __init__(self):
        super(SnakeGame, self).__init__('Snake', SnakeGame.BLACK, window_size=(800,600))
        self.initPlayer()
        self.initEgg()
        self.initBomb()
        self.init()
        self.score = 0
        self.t = 10
        self.initbody()
        self.write_score()

    def initbody(self):
        self.bodyArray = []

    def initPlayer(self):
        self.player = Player(pos = (0,0),
                             color = SnakeGame.WHITE,
                             width = 25,
                             speed = (SnakeGame.V,0))

    def initEgg(self):
        self.egg  = Egg( radius=10, 
                         color=SnakeGame.YELLOW, 
                         pos=(250,250))

    def initBomb(self):
        self.bomb = Bomb(radius=10, 
                         color=SnakeGame.RED, 
                         pos=(500,500))

    def init(self):
        super(SnakeGame, self).init()
        

    def update(self):
        self.t -= 1
        #self.body.update(self.player)
        if self.t <= 0:
            temp = (self.player.x, self.player.y)
            self.player.update()
            for x in range(0,len(self.bodyArray)):
                temp1 = (self.bodyArray[x].x, self.bodyArray[x].y)
                self.bodyArray[x].update(temp[0],temp[1])
                temp = temp1
            self.t = 10
        self.checkInputKey()
        self.catch_egg()
        self.catch_bomb()
       # print "update"

    def catch_egg(self):
        if self.player.catch_egg(self.egg):
            #print"catch"
            self.egg.newPos(800,600)
            self.bomb.newPos(800,600)
            self.score+=1
            self.write_score()
            body = Body(SnakeGame.WHITE)
            self.bodyArray.append(body)
            for x in range(0,len(self.bodyArray)):
                print x
            #print self.score

    def catch_bomb(self):
        if self.player.catch_bomb(self.bomb):
            self.terminate()
            #print"catch bomb"

    def checkInputKey(self):
        if self.is_key_pressed(K_UP):
            self.player.setSpeed(0,-SnakeGame.V)
        elif self.is_key_pressed(K_DOWN):
            self.player.setSpeed(0,SnakeGame.V)
        elif self.is_key_pressed(K_RIGHT):
            self.player.setSpeed(SnakeGame.V,0)
        elif self.is_key_pressed(K_LEFT):
            self.player.setSpeed(-SnakeGame.V,0)

    def render(self, surface):
        self.player.render(surface)
        self.egg.render(surface)
        self.bomb.render(surface)
        surface.blit(self.show_score, (10,10))
        for x in range(0,len(self.bodyArray)):
            self.bodyArray[x].render(surface)
        #print "render"

    def write_score(self):
        self.show_score = self.font.render("Score = %d" % self.score, 0, SnakeGame.WHITE)

def main():
    game = SnakeGame()
    game.run()

if __name__ == '__main__':
    main()
