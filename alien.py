from typing import Any
import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien fleet"""
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #Load image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store the alien's exact horizontal position
        self.x = float(self.rect.x)
        
    
    def check_edges(self):
        """Return True if alien is at the end of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        
        
    def update(self):
        """Move the aliens to the right or left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
        
    
    