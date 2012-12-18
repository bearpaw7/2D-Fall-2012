'''

Tanks - Working Title
First 2D Fall 2012 Game for TAGD Members

'''

import os, sys, time
import pygame
from pygame.locals import *
from math import pi, radians, cos, sin
from sabot import Sabot

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class Tank(pygame.sprite.Sprite):
    # Singleton tank images
    RedTankImage = None
    BlueTankImage = None
    ImageScale = [50, 50]
    DegreesRotated = 5
    MoveRadius = 5
    ReloadTime = 1 # seconds

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
        self.lastSabot = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def inBounds(self, newPosition):
        if newPosition[0] > 0 and newPosition[0] < 800:
            if newPosition[1] > 0 and newPosition[1] < 600:
                return True
            return False
        return False

    def moveForward(self):
        newPosition = [
                            self.rect.center[0] - Tank.MoveRadius * sin( -radians(self.facing) ) , # x position
                            self.rect.center[1] - Tank.MoveRadius * cos( radians(self.facing) )   # y position
                            ]
        #if inBounds(newPosition):
        if(self.inBounds(newPosition)):
            self.rect.center = newPosition
        
    def moveReverse(self):
        newPosition = [
           self.rect.center[0] + Tank.MoveRadius * sin( -radians(self.facing) ) , # x position
           self.rect.center[1] + Tank.MoveRadius * cos( radians(self.facing) )   # y position
        ]
        
        if(self.inBounds(newPosition)):
            self.rect.center = newPosition

    
    def moveTo(self, newPosition, sabot_rect):
        # if the position is match to the bullet, given sabot's rect
        if(self.rect == sabot_rect): 
            self.kill()
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
    
    def shootSabot(self):
        if (time.time() - self.lastSabot) > Tank.ReloadTime:
            self.lastSabot = time.time()
            sabotAngle = -self.facing + 1170 # weird conversion from tank unit circle to sabot unit circle
            s = Sabot(self.rect.center[0], self.rect.center[1], radians(sabotAngle))
            return s
        
    def killTank(self):
        self.kill()

if __name__ == '__main__':
    print '\'tank.py\' is not the correct startup script'
    print 'Attempting to execute main.py...'
    try:
        execfile('main.py')
    finally:
        print 'Exited tank.py'

