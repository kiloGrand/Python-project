import pygame
from pygame import locals
from sys import exit

def main():
    #1 模块初始化
    pygame.init()
    #2 获取绘制屏幕
    screen = pygame.display.set_mode((512,768))
    #8 设置窗口标题
    pygame.display.set_caption("雷霆战机")
    #6 加载背景对象
    background = pygame.image.load("images/bg/bg.jpg")
    #pygame.display.set_icon("images/hero/hero.png")
    #3 游戏主循环
    while True:
        #7 将背景对象绘制到屏幕中
        screen.blit(background,(0,0))
        #4 刷新屏幕
        pygame.display.update()
        #5 事件监听
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
                exit()

if __name__ == '__main__':
    main()



