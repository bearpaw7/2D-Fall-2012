'''
Tanks - Working Title
First 2D Fall 2012 Game for TAGD Members

'''

import pygame
import os
from math import pi

class Tank(pygame.sprite.Sprite):
    # Singleton tank images
    RedTankImage = None
    BlueTankImage = None
    ImageScale = [80, 80]

    def __init__(self, startPosition, joinTeam):
        pygame.sprite.Sprite.__init__(self) #initialize parent class

        if joinTeam == 'red':
            if Tank.RedTankImage == None:
                Tank.RedTankImage = pygame.image.load( os.path.join('images', 'red_tank.png')).convert()
                Tank.RedTankImage = pygame.transform.scale(Tank.RedTankImage, Tank.ImageScale)
            self.image = Tank.RedTankImage
        elif joinTeam == 'blue':
            if Tank.BlueTankImage == None:
                Tank.BlueTankImage = pygame.image.load( os.path.join('images', 'blue_tank.png')).convert()
                Tank.BlueTankImage = pygame.transform.scale(Tank.BlueTankImage, Tank.ImageScale)
            self.image = Tank.BlueTankImage

        self.rect = self.image.get_rect()
        self.rect.topleft = startPosition
        self.team = joinTeam

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def moveTo(self, newPosition):
        self.rect = newPosition

if __name__ == '__main__':
    print '\'tank.py\' is not the correct startup script'
    print 'Attempting to execute main.py...'
    try:
        execfile('main.py')
    finally:
        print 'Exited tank.py'

