"""
以面向对象编程思路实现
通过类的继承重构代码
主要是通过Sprite精灵类的重写实现
主要重写__init__ 以及 update
"""

import pygame
from pygame import locals
from sys import exit
from pygame.sprite import Sprite,Group
import random


class BGSprite(Sprite):                             #背景精灵
    def __init__(self,imagepath):
        super().__init__()
        self.image = pygame.image.load(imagepath)
        self.rect = self.image.get_rect()
class EnemySprite(Sprite):
    def __init__(self,imagepath,rect,pos,speed,screen):
        super().__init__()
        self.image = pygame.image.load(imagepath)
        self.image = self.image.subsurface(rect)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = speed
        self.xspeed = speed
        self.timer = 0
        self.bulletgroup = Group()
        self.screen = screen

    def update(self):
        self.bulletgroup.update()
        self.bulletgroup.draw(self.screen)
        self.timer += 0.01
        if self.timer > 1:
            #print("敌机发射子弹")
            bullet = BulletSprite("images/bullet/enemy_bullet.png",[0,0,15,20],[self.rect.x+45,self.rect.y+39.5],-5)
            self.bulletgroup.add(bullet)
            self.timer = 0
        self.rect.y += self.speed
        self.rect.x += self.xspeed
        if self.rect.x > 400:
            self.xspeed *= -1
            self.rect.x += self.xspeed
        if self.rect.x < 0:
            self.xspeed *= -1
            self.rect.x += self.xspeed
        if self.rect.y > 800:
            self.kill()

class BulletSprite(Sprite):                             #子弹
    def __init__(self,imagepath,rect,pos,speed):
        super().__init__()
        self.image = pygame.image.load(imagepath)
        self.image = self.image.subsurface(rect)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = speed
    def move(self):
        self.rect.y -= self.speed
        if self.rect.y < -50:
            self.kill()
    def update(self):
        self.move()

class PlayerSprite(Sprite):                             #玩家战机
    def __init__(self,imagepath,rect,pos,speed,screen):
        super().__init__()
        self.image = pygame.image.load(imagepath)
        self.image = self.image.subsurface(rect)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = speed
        self.screen = screen
        self.bulletgroup = Group()
        self.score = 0
        self.hp = 10
        self.timer = 0
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[locals.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.x > 412:
                self.rect.x = 412
        if keys[locals.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x = 0
        if keys[locals.K_UP]:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.rect.y = 0
        if keys[locals.K_DOWN]:
            self.rect.y += self.speed
            if self.rect.y > 702:
                self.rect.y = 702
    def fire(self):
        # print("发射子弹")
        bullet = BulletSprite("images/bullet/TMD.png", [0, 0, 21, 59], [self.rect.x + 23, self.rect.y - 20], 6)
        bullet2 = BulletSprite("images/bullet/TMD.png", [0, 0, 21, 59], [self.rect.x + 60, self.rect.y - 20], 6)
        self.bulletgroup.add(bullet)
        self.bulletgroup.add(bullet2)
    def update(self):
        self.bulletgroup.update()
        self.bulletgroup.draw(self.screen)
        self.move()
        self.timer += 1
        if self.timer > 25:
            # print("战机发射子弹")
            bullet = BulletSprite("images/bullet/TMD.png", [0, 0, 21, 59], [self.rect.x + 23, self.rect.y - 20], 6)
            bullet2 = BulletSprite("images/bullet/TMD.png", [0, 0, 21, 59], [self.rect.x + 60, self.rect.y - 20], 6)
            self.bulletgroup.add(bullet)
            self.bulletgroup.add(bullet2)
            self.timer = 0

CREATE_ENEMY = locals.USEREVENT + 1

def main():
    pygame.init()
    pygame.display.set_caption("雷霆战机")
    screen = pygame.display.set_mode((512,768))
    bggroup = Group()
    bgsprite = BGSprite("images/bg/bg.jpg")
    bggroup.add(bgsprite)
    playergroup = Group()
    playersprite = PlayerSprite("images/hero/hero.png",[0,0,100,66],[bgsprite.rect.w/2 - 50 ,600],5,screen)
    playergroup.add(playersprite)
    enemygroup = Group()
    pygame.time.set_timer(CREATE_ENEMY,random.randint(500,1000))
    font = pygame.font.Font(None,32)

    while True:
        bggroup.update()
        bggroup.draw(screen)

        playergroup.update()
        playergroup.draw(screen)

        enemygroup.update()
        enemygroup.draw(screen)

        screen.blit(font.render("Score:"+str(playersprite.score) , True,(255, 0, 0)),(20,20))
        screen.blit(font.render("HP:" + str(playersprite.hp), True, (255, 0, 0)), (20, 60))

        pygame.display.update()

        check1 = pygame.sprite.groupcollide(playersprite.bulletgroup,enemygroup,True,True)#碰撞检测 销毁子弹 销毁敌机
        if check1:
            playersprite.score += 1
        check2 = pygame.sprite.groupcollide(playergroup,enemygroup,False,True)
        if check2:
            playersprite.hp -= 1

        #print(enemygroup)
        for enemy in enemygroup:
            check3 = pygame.sprite.groupcollide(playergroup,enemy.bulletgroup,False,True)
            if check3:
                playersprite.hp -= 1
        if playersprite.hp <= 0:
            playersprite.kill()

        for event in pygame.event.get():
            if event.type == locals.KEYUP:
                if event.key == locals.K_SPACE:
                    playersprite.fire()
            if event.type == locals.QUIT:
                pygame.quit()
                exit()
            if event.type == CREATE_ENEMY:
                enemy = EnemySprite("images/enemy/enemy1.png",[0,0,102,79],[random.randint(0,410),-50],2,screen)
                enemygroup.add(enemy)
        #playersprite.fire() #自动开火


if __name__ == '__main__':
    main()