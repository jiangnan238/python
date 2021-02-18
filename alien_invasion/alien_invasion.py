import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    #初始化游戏
    pygame.init()
    #导入设置
    game_settings = Settings()
    #生成主屏幕screen；第一个参数是屏幕大小，
    # 第二个0表示不使用特性，可用FULLSCREEN,RESIZEBLE,NOFRAME,DOUBLEBUF(双缓冲，使用时需用pygame.display.flip()来刷新屏幕)
    # 32表示色深；
    screen = pygame.display.set_mode(
        (game_settings.screen_width,game_settings.screen_height),0,32)
    #设置窗口标题名称
    pygame.display.set_caption("Alvien Invasion")
   
    #创建飞船
    ship = Ship(screen)

    #主游戏
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #填充背景
        screen.fill(game_settings.background_color)
        #绘制飞船
        ship.blitme()
        #刷新屏幕
        pygame.display.flip()

run_game()