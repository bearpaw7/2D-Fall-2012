'''

wally was here.

add collision detection
'''

import pygame
import os
import math

class Sabot(pygame.sprite.Sprite):
    SabotImage = None
    ImageScale = [50, 50]
    movement = 5

    def __init__(self, x, y, radian):
        pygame.sprite.Sprite.__init__(self)
        if Sabot.SabotImage is None:
            Sabot.SabotImage = pygame.image.load( os.path.join('images', 'sabot.png') ).convert()
            Sabot.SabotImage = pygame.transform.scale(Sabot.SabotImage, Sabot.ImageScale)
        self.image = Sabot.SabotImage
        self.rect = self.image.get_rect()
        self.rect.topleft = [ x, y]
#        given direction as radian 
        self.direction = radian

    def draw(self, screen):
        self.rect.top += Sabot.movement * math.cos(self.direction) 
        self.rect.left += Sabot.movement * math.sin(self.direction)
        
        if(self.rect.top > 0 and self.rect.bottom < screen.get_rect().bottom):
            if(self.rect.left > 0 and self.rect.right <  screen.get_rect().bottom):
                screen.blit(self.image, self.rect)
                
            
        
    

if __name__ == '__main__':
    print '\'sabot.py\' is not the correct startup script'
    print 'Attempting to execute main.py...'
    try:
        execfile('main.py')
    finally:
        print 'Exited sabot.py'
