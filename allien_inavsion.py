import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alliens import Allien
from scoreboard import Scoreboard

from button import Button

from game_stats import GameStats
class AlienInvasion:
    """
    Overall class to manage game assets
    """

    def __init__(self):
        """surface->a part of game screen where elements can be placed
        this surface will be redrawn at every time in game loop return dilay.se_mode()
        """
        self.resetRowCounter=0
        self.setting=Settings()
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
        self.setting.screen_width=self.screen.get_rect().width
        self.setting.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("Allein Invasion")
        self.stats=GameStats(self)
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.alliens=pygame.sprite.Group()
        self._create_fleet()
        self.play_button=Button(self,"Press Enter")
        self.sb=Scoreboard(self)
        pygame.mouse.set_visible(False)
        
    def _ship_hit(self):
        for allien in self.alliens.sprites():
            if allien.rect.bottom==self.screen.get_rect().bottom:
                self.stats.ship_left-=1
                if self.stats.ship_left==0:
                    print("Game end")
                    self.stats.game_active=False
                    self.alliens.empty()
                    self.bullets.empty()
                    self.screen.fill(self.setting.bg_color,self.screen.get_rect())
                    self.alliens.draw(self.screen)
                    self.ship.blitme()
                    self.stats.reset_stats()
                    pygame.display.flip() 
                break

    def _create_fleet(self):
        allien=Allien(self)
        allien_width,allien_height=allien.rect.size
        available_space_x=self.screen.get_width()-(2*allien_width)
        number_alliens_x=available_space_x//(allien_width)
        number_alliens_x=int(number_alliens_x)
        # number_rows = available_space_y // (2 * allien_height)
        for allien_number in range(number_alliens_x):
            allien=Allien(self)
            allien.x=allien_width+allien_width*allien_number   

            allien.rect.x=allien.x
            allien.rect.y = 0
            self.alliens.add(allien)    
            # image for bg self.bg_image=pygame.image.load("./assets/bg.jpeg")
    #function to check for event
    def _check_event(self):
        #this function returns a list of events sice last time this function was called
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                   self.ship.right_movement=True
                elif event.key==pygame.K_LEFT:
                    self.ship.left_movemet=True
                elif event.key==pygame.K_q or event.key==pygame.K_ESCAPE:
                    sys.exit()
                elif event.key==pygame.K_SPACE:
                    self._fire_bullet()
                elif event.key==pygame.K_RETURN:
                    self.stats.game_active=True

            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    self.ship.right_movement=False
                elif event.key==pygame.K_LEFT:
                    self.ship.left_movemet=False

    def _check_fleet_edges(self):
        for allien in self.alliens.sprites():
            if(allien.check_edges()):
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        #     for allien in self.alliens.sprites():
        #     allien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction*=-1

    def _update_alliens(self):
        self.resetRowCounter+=1
        self._check_fleet_edges()
        self.alliens.update()
        if(self.resetRowCounter==1200):
            self.resetRowCounter=0
            self._create_fleet()
        
        if pygame.sprite.spritecollideany(self.ship, self.alliens):
            print("Ship hit!!!")     

    def _fire_bullet(self):
        if len(self.bullets)<self.setting.bullet_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
    #function to update screen
    def _check_bullet_alien_collisions(self):
        collisions=pygame.sprite.groupcollide(self.bullets,self.alliens,True,True)
        if collisions:
            self.stats.score+=50
            self.sb._prep_score()
        if not self.alliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if(bullet.rect.bottom<=0):
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        
        
        
        

    def _update_screen(self):
            self.screen.fill(self.setting.bg_color)
            #for bg image
            # scaled_bg = pygame.transform.scale(self.bg_image, self.screen.get_size())
            # self.screen.blit(scaled_bg, self.screen.get_rect())
            self.ship.blitme()   #draw ship
            self.ship.update_ship_position()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.alliens.draw(self.screen)
            self.sb.showboard()
            self.sb._prep_score()
            #makes the mostly recnetly drawn screen visible
            
            pygame.display.flip()
      
    def run_game(self):
        #main loop for the game
        while True:
            self._check_event()
            if self.stats.game_active:
               self._update_screen()
               self._update_bullet()
               self._update_alliens()
               self._ship_hit()
               
            else:
                self.screen.fill(self.setting.bg_color,self.screen.get_rect())
                self.alliens.draw(self.screen)
                self.ship.blitme()
                self.play_button.draw_button()
                self.sb.showboard()
                pygame.display.flip()
            
                
            # self._fire_bullet()  for contineous fire

if __name__=='__main__':

    ai=AlienInvasion()
    ai.run_game()