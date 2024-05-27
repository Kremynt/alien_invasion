class GameStats:
    """Track statistics for Alien invasion game"""
    
    def __init__(self,ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        
        #Start Alien invasion in active state
        self.game_active = False
        
        
    def reset_stats(self):
        """initialize statistics that change during game"""
        self.ships_left = self.settings.ship_limit
        