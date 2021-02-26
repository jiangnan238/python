import pygame

class Ship():
    def __init__(self,game_settings,screen):
        #_int_是4个下划线
        self.screen = screen
        self.game_settings = game_settings
        #加载图像
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #设定位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #飞船属性
        self.center = float(self.rect.centerx)

        #持续移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        #移动标志为true并且飞船右坐标小于屏幕右边界
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed
        if self.moving_left and self.rect.left > 0 :
            self.center -= self.game_settings.ship_speed

        #根据self.center更新位置
        self.rect.centerx = self.center