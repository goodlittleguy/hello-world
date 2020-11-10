import pygame
from pygame.sprite import Group
from ship import Ship
class Border():
    def __init__(self,states,setting,screen):
        self.text_color = (20,50,200)
        self.screen = screen
        self.font = pygame.font.SysFont(None,48)
        self.prep_image(setting,states)
        self.prep_high_score(states,setting)
        self.prep_level_score(states,setting)

        self.prep_ship(states, screen, setting)

    def prep_image(self,setting,states):

        self.original_score = int(round(states.score,-1))
        self.score = "{:,}".format(self.original_score)
        self.image_load = self.font.render(self.score,True,self.text_color,setting.cl)
        self.image_load_rect = self.image_load.get_rect()
        self.image_load_rect.right = setting.sw - 20
        self.image_load_rect.top =  20

    def prep_high_score(self,states,setting):
        self.original_high_score = int(round(states.high_score, -1))
        self.high_score = "{:,}".format(self.original_score)
        self.high_score_image = self.font.render(self.high_score,True,self.text_color,setting.cl)
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.centerx = int(setting.sw/2)
        self.high_score_image_rect.top =  20

    def prep_level_score(self,states,setting):
        self.level_str = str(states.level)
        self.level_iamge = self.font.render(self.level_str,True,self.text_color,setting.cl)
        self.level_iamge_rect = self.level_iamge.get_rect()
        self.level_iamge_rect.bottom = setting.sh
        self.level_iamge_rect.centerx = int(setting.sw/2)

    def prep_ship(self,states,screen,setting):
        self.ships = Group()
        for i in range(states.limited_bullets):
            new_ship = Ship(screen,setting)
            new_ship_rect = new_ship.rt_ship
            new_ship_rect.left = new_ship_rect.width * i + 5
            new_ship_rect.top = 0
            self.ships.add(new_ship)


    def blitme(self):
        self.screen.blit(self.image_load,self.image_load_rect)
        self.screen.blit(self.high_score_image,self.high_score_image_rect)
        self.screen.blit(self.level_iamge,self.level_iamge_rect)
        for i in self.ships:
            i.blitme()