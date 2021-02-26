import sys
import pygame

#设置屏幕尺寸
screen = pygame.display.set_mode((900,1000), 0)
#设置标题
pygame.display.set_caption('A gril')
#设置背景颜色
screen_color = (0,0,0)
#加载图片（位置使用/）
image = pygame.image.load("role/images/gril.bmp")
#获取图片尺寸
image_rect = image.get_rect()
#获取屏幕尺寸
screen_rect = screen.get_rect()

#设置位置
image_rect.centerx = screen_rect.centerx
image_rect.centery = screen_rect.centery

while True:
    screen.blit(image, image_rect)#绘制图片
    pygame.display.flip()#刷新屏幕
    for event in pygame.event.get():#获取事件
        if event.type == pygame.QUIT:#检测到关闭窗口退出
            sys.exit()    