import pygame.font

class Scoreboard:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()

        self.setting=ai_game.setting
        self.stats=ai_game.stats

        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont("Arial",48)

        self._prep_score()


    def _prep_score(self):
       score_str = str(self.stats.score)
    
    # Render the score text
       self.score_image = self.font.render(score_str, True, self.text_color, self.setting.bg_color)
    
    # Get the rect of the score image
       self.score_rect = self.score_image.get_rect()
    
    # Position it in the top-right corner with padding
       self.score_rect.right = self.screen_rect.right - 20
       self.score_rect.top = 20



    def showboard(self):
        self.screen.blit(self.score_image,self.score_rect)