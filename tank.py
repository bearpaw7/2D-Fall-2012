'''
Tanks - Working Title
First 2D Fall 2012 Game for TAGD Members

'''

import os, sys
import pygame
from pygame.locals import *
from math import pi, radians, cos, sin

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class Tank(pygame.sprite.Sprite):
    # Singleton tank images
    RedTankImage = None
    BlueTankImage = None
    ImageScale = [80, 80]
    DegreesRotated = 5
    MoveRadius = 5

    def __init__(self, startPosition, joinTeam):
        pygame.sprite.Sprite.__init__(self) #initialize parent class

        if joinTeam == 'red':
            if Tank.RedTankImage == None:
                Tank.RedTankImage = pygame.image.load( os.path.join('images', 'red_tank.png')).convert_alpha()
                Tank.RedTankImage = pygame.transform.scale(Tank.RedTankImage, Tank.ImageScale)
            self.image = Tank.RedTankImage
        elif joinTeam == 'blue':
            if Tank.BlueTankImage == None:
                Tank.BlueTankImage = pygame.image.load( os.path.join('images', 'blue_tank.png')).convert_alpha()
                Tank.BlueTankImage = pygame.transform.scale(Tank.BlueTankImage, Tank.ImageScale)
            self.image = Tank.BlueTankImage

        self.rect = self.image.get_rect()
        self.rect.center = startPosition
        self.team = joinTeam
        self.facing = 0 # degrees

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def moveForward(self):
        self.rect.center = [
                            self.rect.center[0] - Tank.MoveRadius * sin( -radians(self.facing) ) , # x position
                            self.rect.center[1] - Tank.MoveRadius * cos( radians(self.facing) )   # y position
                            ]
        
    def moveReverse(self):
        self.rect.center = [
                            self.rect.center[0] + Tank.MoveRadius * sin( -radians(self.facing) ) , # x position
                            self.rect.center[1] + Tank.MoveRadius * cos( radians(self.facing) )   # y position
                            ]
        
    def moveTo(self, newPosition):
        self.rect.center = newPosition
    
    def rotateLeft(self):
        self.facing += Tank.DegreesRotated
        self.rotateTo(self.facing)
    
    def rotateRight(self):
        self.facing -= Tank.DegreesRotated
        self.rotateTo(self.facing)
        
    def rotateTo(self, degrees):
        # rotate a Surface, maintaining position
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate( Tank.RedTankImage, -degrees )
        self.rect = self.image.get_rect(center = oldCenter)
        print "angle", self.facing, ", center", self.rect.center

if __name__ == '__main__':
    print '\'tank.py\' is not the correct startup script'
    print 'Attempting to execute main.py...'
    try:
        execfile('main.py')
    finally:
        print 'Exited tank.py'

