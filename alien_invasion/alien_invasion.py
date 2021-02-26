import pygame
import game_functions as gf
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
    ship = Ship(game_settings,screen)

    #主游戏
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(game_settings,screen,ship)
run_game()