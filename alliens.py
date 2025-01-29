import pygame
from pygame.sprite import Sprite
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

class Allien(Sprite):
    def __init__(self,ai_game):
        super().__init__()

        self.screen=ai_game.screen
        self.setting=ai_game.setting

        #load image
        imagePath=resource_path("./assets/allien.bmp")
        self.image=pygame.image.load(imagePath)
        original_width,original_height=self.image.get_size()
        load_factor=0.35

        new_width=(original_width*load_factor)
        new_height=(original_height*load_factor)
        self.image=pygame.transform.scale(self.image,(new_width,new_height))
        self.rect=self.image.get_rect()
        
        self.rect.x=self.rect.width
        self.rect.y=0 

        #excat horizental position
        self.initialY=self.rect.y
        self.x=float(self.rect.x)
        self.count=-10

    def check_edges(self):
        screen_rect=self.screen.get_rect()

        if self.rect.right>=screen_rect.right or self.rect.left<= screen_rect.left:
            return True

    def update(self):
        self.count+=1
        self.x+=(self.setting.allien_speed*self.setting.fleet_direction)
        self.rect.x=self.x
        #speed control
        if self.count%12==0:
            self.rect.y += self.setting.fleet_drop_speed
        
        