import pygame, sys
from src.player import Player
from src.enemies import Enemies


img_file = "assets/pygame_background.png"

class Controller: 
    def __init__(self):
        """
        docstring
        """
        pygame.init()
        pygame.event.pump()
        pygame.display.init()
        self.clock = pygame.time.Clock()
        self.width = 1000
        self.height = 800
        self.window = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.image.load(img_file)
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.player = Player()
        self.player.image = pygame.transform.scale(self.player.image, (100, 100))     # Scale
        self.enemy = Enemies()
        self.enemy.image = pygame.transform.scale(self.enemy.image, (250, 250))
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player, self.enemy)
        
    def mainloop(self):
        """
        docstring
        """
        running = True
        while running: 
            #1. Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        running = False
                
                if event.type == pygame.KEYDOWN:  
                    pygame.key.set_repeat(75)
                    if event.key == pygame.K_RIGHT:           # Why do functions not work
                        self.player.move_right()
                    elif event.key == pygame.K_LEFT:
                        self.player.move_left()
                    elif event.key == pygame.K_UP:
                        pygame.key.set_repeat(0)
                        self.player.jumping()
                        pygame.time.wait(1000)
                        self.player.not_jumping()
                        


            #4. Display next frame
            pygame.display.flip()
            self.window.blit(self.background, (0, 0))          # Puts it onto screen                  
            self.sprites.draw(self.window)                     # Draws the sprites onto window
            self.sprites.update()
            self.clock.tick(30)
            
        pygame.quit()
        sys.exit()



#2. detect collisions and update models

#3. Redraw next frame

#4. Display next frame