import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from ship"""
    
    def __init__(self,ai_game):
        """Create a bullet object at ship's current location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        #Create bullet at rect(0,0) and set to ship location
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #Store bullet position as a decimal
        self.y = float(self.rect.y)
        
        
    def update(self):
        """Move bullet up the screen"""
        self.y -= self.settings.bullet_speed
        #Update rect position
        self.rect.y = self.y
        
        
    def draw_bullet(self):
        """Draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)