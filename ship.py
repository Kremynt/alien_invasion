import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship"""
    
    def __init__(self,ai_game):
        """Initialize ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        #Load screen and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #start each new ship at the bottom of the center of thr screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        #Store decimal value for ship's horizontal position
        self.x = float(self.rect.x)
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        
        
        
    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
        
    def update(self):
        """update ship's position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        #Update rect object from self.x
        self.rect.x = self.x
        
        
    def blitme(self):
        """draw the ship at its curent location"""
        self.screen.blit(self.image,self.rect)
        
        