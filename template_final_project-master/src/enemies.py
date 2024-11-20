class Enemies:
    def __init__(self):
        self.move = True
    
    def __init__(self, x, y, img_file):
        '''
        Initializes enemy object
        args:
         - x: int - starting x coordinte
         - y: int - starting y coordintate
         - img: str - path to img file of enemy
        '''
        
        # self.not_jumping = True
        # self.x = x
        # self.y = y
        # self.img = img_file
        
    def moving(self):
        '''
        Moves back and forth along the platform
        args: None
        return: None
        '''
        pass
    
    def shoot(self):
        '''
        Shoots a bullet object at the player to try and kill them
        args: None
        return: bullet
        '''
        pass
    
    def turn(self):
        '''
        Turns automatically toward the player instead of facing one direction
        args: None
        return: None
        '''
        pass