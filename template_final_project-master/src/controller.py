import pygame
import sys


class Controller: 
    def __init__(self):
        """
        docstring
        """
        
    def mainloop(self):
        """
        docstring
        """
        running = True
        while running: #this can also be a variable instead of just True
            #1. Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        running = False
                
                
            #2. detect collisions and update models

            #3. Redraw next frame

            #4. Display next frame
            pygame.display.flip()
            
pygame.quit()
sys.exit()