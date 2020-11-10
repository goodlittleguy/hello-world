import pygame
class Button():
    def __init__(self,screen,msg):
        self.screen = screen
        self.rt_s = self.screen.get_rect()

        self.button_w,self.button_h = 30,10
        self.rect =pygame.Rect(0,0,self.button_w,self.button_h)
        self.rect.center = self.rt_s.center
        self.button_c =(0,255,0)
        self.text_c =(255,255,255)

        self.font = pygame.font.SysFont(None,48)
        self.print_image(msg)

    def print_image(self,msg):
        self.msy_image = self.font.render(msg,True,self.text_c,self.button_c)
        self.msy_image_rect = self.msy_image.get_rect()
        self.msy_image_rect.center = self.rt_s.center

    def blitme(self):
        self.screen.fill(self.button_c,self.rect)
        self.screen.blit(self.msy_image,self.msy_image_rect)
