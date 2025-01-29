import pygame
from settings import Settings
class GameStats:
    def __init__(self,ai_game):
       self.setting=Settings()
       self.reset_stats()
       self.game_active=False
       self.score=0


    def reset_stats(self):
        #reset game changes
        self.ship_left=self.setting.ship_limit
        self.score=0
