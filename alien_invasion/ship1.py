import pygame 

class Ship():
    def __init__(self, screen): #_int_不是下划线，使用智能补全的横线
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('alien_invasion/images/ship.bmp') 
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() 
        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self): 
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)