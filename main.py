'''
   
Tanks - Working Title
First 2D Fall 2012 Game for TAGD Members

'''

import pygame
import os
import math
import time
from sabot import Sabot 
from tank import Tank

SCREEN_SIZE = [800,600]

class MainWindow:
    sprites = pygame.sprite.Group()
    
    def userInput(self, event, tankPosition):
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            self.dx = 0
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            self.dx = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.dx = -1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.dx = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            self.dy = 0
        elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            self.dy = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.dy = 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            self.dy = -1
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            self.dz = 0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.dz = 1
    
    def userAttack(self):
        if self.dz == 1:
            if (time.time() - self.dzTime) > 1:
                self.dzTime = time.time()
                self.sprites.add(Sabot(self.localTank.rect[0], self.localTank.rect[1], math.pi))
    
    def __init__(self):
        print 'Initiated main window'
        
        # Define the colors we will use in RGB format
        black = [  0,  0,  0]
        white = [255,255,255]
        self.dx = 0  # x travel
        self.dy = 0  # y travel
        self.dz = 0  # shot firing
        self.dzTime = 0 # shot last fired
        self.speed = 3 # tank speed
        pygame.init()
        screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Tanks Title") #FIXME working title
        
        # Initialize timer for MainWindow
        clock = pygame.time.Clock()
        
        font = pygame.font.Font(None, 25)
        # Render the text. "True" means anti-aliased text.
        # Black is the color. This creates an image of the
        # letters, but does not put it on the screen
        text = font.render("Tanks - hello world", True, black)
        
        tankPosition = [100, 100]
        self.localTank = Tank(tankPosition, "red")
        
        testSabot = Sabot( 200,200, math.pi)
        
        mainExit=False
        while mainExit==False:
            # This limits the while loop to a max of 45 times per second.
            # Leave this out and we will use all CPU we can.
            clock.tick(45)
            
            for event in pygame.event.get(): # User did something
                # If user clicked close or hit escape key
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    mainExit = True # Flag that we are done so we exit this loop
                # FIXME Add menu system here
                self.userInput(event, tankPosition)
            # Put the image of the text on the screen at 250x250
            screen.fill(white)
            screen.blit(text, [250,250])
            
            # update the tank position
#            tankPosition = [tankPosition[0] + (self.dx * self.speed), tankPosition[1] + (self.dy * self.speed)]
#            self.localTank.moveTo(tankPosition)
            if self.dy > 0:
                self.localTank.moveForward()
            elif self.dy < 0:
                self.localTank.moveReverse()
            if self.dx > 0:
                self.localTank.rotateLeft()
            elif self.dx < 0:
                self.localTank.rotateRight()
            # paint the tank
            screen.blit(self.localTank.image, self.localTank.rect)
            
            testSabot.draw(screen)
            self.userAttack()
            for shot in self.sprites.sprites():
                shot.draw(screen)
            # Go ahead and update the screen with what we've drawn.
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()
        
    
if __name__ == '__main__':
    print 'Working Directory: ', os.getcwd()
    MainWindow()
    print 'Exited MainWindow'

