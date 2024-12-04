import pygame

class Platforms(pygame.sprite.Sprite):
    def __init__(self, x, y):
        '''
        Initializes platform object
        args: None
        return: None
        '''
        super().__init__()
        self.image = pygame.image.load("assets/platform.png")   
        self.image = pygame.transform.scale(self.image, (200, 25))
        self.rect = self.image.get_rect()
        self.rect = self.rect.scale_by(1, 0.8)
        self.x = x
        self.y = y
        self.rect.center = [self.x, self.y]
        
    def return_point_right(self):
        self.right = self.x + 100
        self.mid_height = self.y + 12.5 
        self.my_point = (self.right, self.mid_height)
        return self.my_point
    
    def return_point_left(self):
        self.left = self.x - 100
        self.mid_height = self.y + 12.5
        self.my_point = (self.left, self.mid_height)
        return self.my_point
    
    def return_point_under(self):
        self.mid_height = self.y + 12.5
        self.under_pt_left = self.x - 50
        self.under_pt_right = self.x + 50
        return (self.under_pt_left, self.mid_height), (self.under_pt_right, self.mid_height)