import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        '''
        Initializes player object
        args:
         - x: int - starting x coordinte
         - y: int - starting y coordintate
         - img: str - path to img file of player
        '''
        super().__init__()
        self.p_jumping = False
        self.image = pygame.image.load("assets/water_girl.png")   # Puts image on screen (dont reuse variable names)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [200, 620]          # Centers it at [200, 660]
        self.speed_side = 10
        self.speed_down = 0.5
        
    def move_right(self):
        '''
        Moves right when right arrow key is pressed until let go
        args: None
        return: None
        '''
        self.rect.x += self.speed_side
    
    def move_left(self):
        self.rect.x -= self.speed_side
        '''
        Moves left when left arrow key is pressed until let go
        args: None
        return: None
        '''
    
    def down(self):
        self.rect.y += self.speed_side
    
    def jumping(self):
        self.rect.y -= self.speed_side
        '''
        Moves up 1 when space or up arrow key is pressed
        args: None
        return: None
        '''
    
    def falling(self):
        self.rect.y += self.speed_down
    
    def not_jumping(self):
        self.rect.y += self.speed_side
    
    def block(self):        # Hypothetical
        '''
        Blocks attack when shift key is presed  
        args: None
        return: None
        '''
        pass