import sys
import pygame
def run_game():
    "初始化游戏，并创建屏幕对象"
    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    "开始游戏主循环"
    while True:
        #监视键盘和鼠标事件
        for even in pygame.event.get():
            if even.type==pygame.QUIT:
                sys.exit()
        #pygame.display.flip()
run_game()
    
