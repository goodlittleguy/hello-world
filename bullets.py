import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,setting,ship,screen):
        super(Bullet,self).__init__()
        self.screen =screen
        self.bullte_speed = setting.bullet_speed
        self.bh = setting.bh
        self.bw = setting.bw
        self.bcl = setting.bcl
        self.rect = pygame.Rect(0,0,self.bw,self.bh)
        self.rt_b = self.rect
        self.rt_b.bottom = ship.rt_ship.top
        self.rt_b.centerx = ship.rt_ship.centerx
        self.y = float(self.rt_b.y)

    def update(self):
        self.y -= self.bullte_speed
        self.rt_b.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.bcl,self.rt_b)