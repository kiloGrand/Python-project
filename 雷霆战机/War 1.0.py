import pygame
from pygame import locals
from sys import exit

def main():
    #1 初始化pygame模块
    pygame.init()
    #2 获取绘制窗口
    screen = pygame.display.set_mode((512,768))
    pygame.display.set_caption("雷霆战机")
    #3 游戏使用主循环
    while True:
        #4 刷新游戏屏幕
        pygame.display.update()
        #5 监听游戏事件
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
                exit()

if __name__ == '__main__':
    """
    定义项目入口函数
    """
    main()