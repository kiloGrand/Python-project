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
    print(background.get_rect())
    #pygame.display.set_icon("images/hero/hero.png")
    #9 加载我方飞机
    player = pygame.image.load("images/hero/hero.png")    #使用单独的图片
    #allimage = pygame.image.load("images/hero/shoot.png")   #加载共享大图
    #player = allimage.subsurface(0,99,102,106)    #从共享大图中加载玩家飞机
    playerpos = (background.get_rect().w/2 - player.get_rect().w/2,600)#居中公式
    #print("777"+playerpos)
    #3 游戏主循环
    while True:
        #7 将背景对象绘制到屏幕中
        screen.blit(background,(0,0))
        # 10 绘制我方飞机
        screen.blit(player, playerpos)
        #4 刷新屏幕
        pygame.display.update()
        #5 事件监听
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
                exit()

if __name__ == '__main__':
    main()



