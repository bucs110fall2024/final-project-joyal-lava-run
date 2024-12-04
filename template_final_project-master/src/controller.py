import pygame, sys, time
import pygame_menu
from src.player import Player
from src.enemies import Enemies
from src.platforms import Platforms
from src.lava import Lava
from src.goku import Goku
from src.shoot import Shoot
from src.helicopter import Helicopter
from src.collision_plat import Collision_Plat
from src.winner import Winner
from src.game_over import GameOver

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
        pygame.display.set_caption("Lava Run")
        self.background = pygame.image.load(img_file)
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.player = Player()
        self.enemy = Enemies()
        self.lava = Lava()
        self.goku = Goku()
        self.shoot = Shoot()
        self.helicopter = Helicopter()
        self.winner = Winner()
        self.game_over = GameOver()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player, self.enemy, self.goku , self.shoot, self.helicopter)
        self.ball_sprites = pygame.sprite.Group()
        self.plat_sprites = pygame.sprite.Group()
        self.x_cord = [200, 500, 800, 500, 200, 500, 800, 500, 200, 500]
        self.y_cord = 700
        self.plat_list = []
        self.ball_list = []
        self.coll_list = []
        for _ in range(10):
            self.new_plat = Platforms(x = self.x_cord[_], y = self.y_cord)
            self.plat_sprites.add(self.new_plat)
            self.plat_list.append(self.new_plat)
            self.y_cord -= 68
        self.y_cord = 700
        for _ in range(10):
            self.collision_plat = Collision_Plat(x = self.x_cord[_], y = self.y_cord)
            self.coll_list.append(self.collision_plat)
            self.y_cord -= 68
        self.LAVA_RISE = pygame.USEREVENT +1
        self.sprites.add(self.lava)                        # Add last
        self.winning = False
        self.loser = False
        self.state = "START"
        
    def menu_loop(self):
        menu = pygame_menu.Menu('Lava Run', 400, 300)
        menu.add.text_input('Name :', default='Player 1', maxchar=20)
        menu.add.label("Press SPACE to begin")
        menu.mainloop(self.window)
        while self.state == "START":
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Controller.mainloop()
        
    def mainloop(self):
        """
        docstring
        """
        self.time_ms = 0
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
                    pygame.key.set_repeat(100)
                    if event.key == pygame.K_d:       
                        self.player.move_right()
                    elif event.key == pygame.K_a:
                        self.player.move_left()
                    elif event.key == pygame.K_w:
                        self.player.jumping()
                    elif event.key == pygame.K_s:
                        self.player.down()
                if not event.type == pygame.KEYDOWN:
                    self.player.speed_down = 0.5
                    self.player.falling()
                    
                pygame.time.set_timer(self.LAVA_RISE, 150)
                if event.type == self.LAVA_RISE:
                    self.lava.moving()
                
                self.enemy.moving()

                self.time_ms += 10
                if self.time_ms % 250 == 0:
                    self.new_ball = Shoot()
                    self.sprites.add(self.new_ball)
                    self.ball_sprites.add(self.new_ball)
                    self.ball_list.append(self.new_ball)
                    self.ball_sprites.update()
                
                '''Ways to lose'''
                
                if self.player.rect.right > 1000 or self.player.rect.left < 0:
                    self.player.kill()
                    self.loser = True
                
                if self.player.rect.bottom > 800:
                    self.player.kill()
                    self.loser = True
                
                for balls in self.ball_list:
                    if self.player.rect.colliderect(balls):
                        self.player.kill()
                        self.loser = True
                
                if self.player.rect.colliderect(self.lava.rect):
                    self.player.kill()
                    self.loser = True
                if self.player.rect.colliderect(self.shoot.rect):
                    self.player.kill()
                    self.loser = True
                if self.player.rect.colliderect(self.goku.rect):
                    self.player.kill()
                    self.loser = True    
                    
                if self.player.rect.colliderect(self.helicopter.rect):
                    self.winning = True
                    
                if self.winning == True:
                    self.sprites.add(self.winner)
                    self.sprites.remove(self.lava)
                    self.sprites.add(self.lava)
                    pygame.time.set_timer(self.LAVA_RISE, 50)
                elif self.loser == True:
                    self.sprites.add(self.game_over)
                    self.sprites.remove(self.lava)
                    self.sprites.add(self.lava)
                    pygame.time.set_timer(self.LAVA_RISE, 50)
            
            #4. Display next frame
            pygame.display.flip()
            self.sprites.update()
            self.window.blit(self.background, (0, 0))          # Puts it onto screen                  
            self.plat_sprites.draw(self.window)
            for self.iter_plats in self.coll_list:
                pygame.draw.rect(self.window, (0, 0, 255), self.iter_plats)
            self.sprites.draw(self.window)                     # Draws the sprites onto window
            self.clock.tick(60)
            
        pygame.quit()
        sys.exit()

'''
Creating new plats: can i use list of coords bc they r all the same size
creating enemies on those plats
repeating ball shot 

Problems:
 - shot ball speeds up
 - inversing player speed will cause it to bounce when colliding with top of plat, player TOP not hitting
 - jumping mechanic
 - collision mechanics and falling gravity mechanics
 - hold down and lava stops (tick problem)
 - waiting
 - very hard game
 - how to inherit enemies class into goku
 - shoot isnt callable in goku class
 - every rect is a box
'''
'''
solutions:
- pygame.collisions.mask
- pygame.modulo and see if you can use time (secs) instead of tics
'''


#2. detect collisions and update models

#3. Redraw next frame

#4. Display next frame