import pygame
import os
import math 

class Sabot(pygame.sprite.Sprite):
    image = None
    movement = 5
    
    
    def __init__(self, x, y, radian):
        pygame.sprite.Sprite.__init__(self)
        if Sabot.image is None:
            Sabot.image = pygame.image.load( os.path.join('images', 'sabot.png') ).convert()
        self.image = Sabot.image
#        self.rect = self.image.rect
        self.rect.topleft = [ x, y]
#        given direction as radian 
        self.direction = radian
        
#    def top(self):
#        return self.position[1]
#    def bottom(self):
#        return self.position[1]+self.
#    def left(self):
#        return self.position[0]
#    def right(self):
#        return self.position[0]+self.image.get_width()
#    
    def draw(self, screen):
        self.rect.top += movement * math.cos(self.direction) 
        self.rect.left += movement * math.sin(self.direction)
        
        if(self.top > screen.top and self.bottom < screen.bottom):
            if(self.left > screen.left and self.right <  screen.bottom):
                screen.blit(self.image, self.rect)
                
                
        
        