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
from network import Network

SCREEN_SIZE = [800,600]

class MainWindow:

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
    
    def __init__(self):
        print 'Initiated main window'
        
        # Define the colors we will use in RGB format
        black = [  0,  0,  0]
        white = [255,255,255]
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
        
        net = Network(True) # Start as server
        localAddress = net.getExternalIP()
        print localAddress[0]
        
        tankPosition = [100, 100]
        self.localTank = Tank(tankPosition, "red")
        
        testSabot = Sabot(200,200, math.pi)
        
        mainExit = False
        while mainExit == False:
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
            
            # paint the tank
            screen.blit(self.localTank.image, self.localTank.rect)
            testSabot.draw(screen)
            # Go ahead and update the screen with what we've drawn.
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()
        
    
if __name__ == '__main__':
    print 'Working Directory: ', os.getcwd()
    MainWindow()
    print 'Exited MainWindow'

