import pygame
import os
import sys

def resource_path(relative_path):
    """Get the absolute path to a resource, works for both development and PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores the path in `_MEIPASS`
        base_path = sys._MEIPASS
    except AttributeError:
        # If not running as an .exe, use the current directory
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Ship:
    def __init__(self,ai_game):
        #initiatlizing ship and its starting posstion
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.setting=ai_game.setting
        #loading ship image and get its recatangle
        imagePath=resource_path("./assets/ship.bmp")
        self.image=pygame.image.load(imagePath)

        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)

        self.right_movement=False
        self.left_movemet=False

        #start new ship at bottom center of screen
        
    def update_ship_position(self):
        if self.right_movement and self.rect.right<self.screen_rect.right:
            self.x+=self.setting.ship_speed
        elif self.left_movemet and self.rect.left>0:
            self.x-=self.setting.ship_speed
        self.rect.x=self.x
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)