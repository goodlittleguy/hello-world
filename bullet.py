import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    "对飞船发射子弹进行管理的类"
    def __init__(self,ai_settings,screen,ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height) #在屏幕左上角（0,0）上创建子弹宽3，高3的矩形
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        """向上移动子弹"""
        self.y -= self.speed_factor #更新子弹位置的小数值
        self.rect.y = self.y
    def draw_bullets(self):
        """在屏幕绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
