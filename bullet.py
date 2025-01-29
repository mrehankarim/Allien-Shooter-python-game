import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired by ship"""

    def __init__(self,ai_game):
        """create a bllet object at ship's current position"""
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.setting
        self.color=self.settings.bullet_color

        #current bullet position at (0,0) and then set the curent position

        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop=ai_game.ship.rect.midtop

        #store bullet position as float

        self.y=float(self.rect.y)

    def update(self):
            #update exact position at the bullet
        self.y-=self.settings.bullet_speed
           #update rect position
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)