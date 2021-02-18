import pygame

class Ship():
    def __init__(self,screen):
        #_int_是4个下划线
        self.screen = screen

        #加载图像
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #设定位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)
