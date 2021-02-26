import sys
import pygame
           
def check_keydown_events(event,ship):
        if event.key == pygame.K_RIGHT:#方向键右键按下
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True

def check_keyup_events(event,ship):        
        if event.key == pygame.K_RIGHT:#方向键右键松开
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def check_events(ship):
    #按键和鼠标响应事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#检测到点击退出按钮
            sys.exit()
        elif event.type == pygame.KEYUP:#检测到键盘松开
            check_keyup_events(event,ship)
        elif event.type == pygame.KEYDOWN:#检测到键盘被按下
            check_keydown_events(event,ship)
        
def update_screen(game_settings,screen,ship):
        #填充背景
        screen.fill(game_settings.background_color)
        #绘制飞船
        ship.blitme()
        #刷新屏幕
        pygame.display.flip()       