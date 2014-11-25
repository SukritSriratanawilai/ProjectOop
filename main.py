import pygame
from pygame.locals import *
from gamelib import SimpleGame
from elements import *

class SnakeGame(SimpleGame):
    
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    YELLOW = pygame.Color('yellow')

    def __init__(self):
        super(SnakeGame, self).__init__('Snake', SnakeGame.BLACK)
        self.player = Player(pos = (0,0),
                             color = SnakeGame.WHITE,
                             width = 25,
                             speed = (2.5,0))
        self.egg = Egg(radius=10, 
                        color=SnakeGame.YELLOW, 
                        pos=(100,100))

    def init(self):
        super(SnakeGame, self).init()

    def update(self):
        self.player.update()
        if self.is_key_pressed(K_UP):
            self.player.setSpeed(0,-2.5)
        elif self.is_key_pressed(K_DOWN):
            self.player.setSpeed(0,2.5)
        elif self.is_key_pressed(K_RIGHT):
            self.player.setSpeed(2.5,0)
        elif self.is_key_pressed(K_LEFT):
            self.player.setSpeed(-2.5,0)
       # print "update"

    def render(self, surface):
        self.player.render(surface)
        self.egg.render(surface)
        #print "render"

def main():
    game = SnakeGame()
    game.run()

if __name__ == '__main__':
    main()
