class Settings:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=600
        self.bg_color=(10, 10, 50)
        self.ship_speed=1.5

        #Bullet Settings
        
        self.bullet_speed=3.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(0, 255, 255)
        self.bullet_allowed=3
        self.allien_speed=0.5

        self.fleet_drop_speed=0.7

        #1->right and -1->left
        self.fleet_direction=1

        self.ship_limit = 1