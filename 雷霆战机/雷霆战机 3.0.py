# coding:UTF-8
import pygame
from pygame import locals
from sys import exit
from pygame.sprite import Sprite,Group
import random , time , math


class BGSprite(Sprite):                             #背景精灵
    def __init__(self,imagepath):
        super().__init__()
        self.image = pygame.image.load(imagepath)
        self.rect = self.image.get_rect()

class EnemySprite(Sprite):                          #敌方战机
    def __init__(self,imagepath,pos,speed,screen,movetype,bullettype,hp):
        super().__init__()
        self.image = pygame.image.load(imagepath)
        # self.image = self.image.subsurface(rect)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = speed
        self.xspeed = random.randint(0,speed+1) * movetype
        self.timer = 0
        self.timer2 = 3
        self.bulletgroup = Group()
        self.screen = screen
        self.bullettype = bullettype
        self.hp = hp

    def update(self):
        self.bulletgroup.update()
        self.bulletgroup.draw(self.screen)
        if self.bullettype == 0:
            self.timer += 0.01
            if self.timer > 1:
                # print("敌机发射子弹")
                bullet = EnemyBulletSprite("images/bullet/enemy_bullet1.png", [self.rect.x + 40, self.rect.y + 39.5],
                                           -2, 0)
                bullet2 = EnemyBulletSprite("images/bullet/enemy_bullet1.png", [self.rect.x + 40, self.rect.y + 39.5],
                                            -2, -1)
                bullet3 = EnemyBulletSprite("images/bullet/enemy_bullet1.png", [self.rect.x + 40, self.rect.y + 39.5],
                                            -2, 1)
                self.bulletgroup.add(bullet)
                self.bulletgroup.add(bullet2)
                self.bulletgroup.add(bullet3)
                self.timer = 0
        else:
            self.timer += 0.01
            self.timer2 += 0.01
            if self.timer > 1:
                bullet = EnemyBulletSprite("images/bullet/enemy_bullet2.png", [self.rect.x + 40, self.rect.y + 39.5],-2, -1)
                bullet2 = EnemyBulletSprite("images/bullet/enemy_bullet2.png", [self.rect.x + 120, self.rect.y + 39.5],-2, 1)
                self.bulletgroup.add(bullet)
                self.bulletgroup.add(bullet2)
                self.timer = 0
            if self.timer2 > 4:     #BOSS发射导弹
                bullet = EnemyBulletSprite("images/bullet/boss_bullet.png", [self.rect.x + 80, self.rect.y + 39.5],-2, 0)
                self.bulletgroup.add(bullet)
                self.timer2 = 0
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

    def bomb(self):
        bombimages = ["images/boom/boom01.png",
                      "images/boom/boom02.png",
                      "images/boom/boom03.png",
                      "images/boom/boom04.png",
                      "images/boom/boom05.png",
                      "images/boom/boom06.png",
                           ]
        for i in bombimages :
            self.screen.blit(pygame.image.load(i),(self.rect.x,self.rect.y))
            time.sleep(0.005)
            pygame.display.update()
        self.kill()

class BulletHelp(Sprite):                               #补给品
    def __init__(self,imagepath,rect,pos,speed,screen,movetype):
        super().__init__()
        self.image = pygame.image.load(imagepath)
        self.image = self.image.subsurface(rect)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = speed
        self.xspeed = random.randint(0, speed) * movetype
        self.screen = screen
    def update(self):
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

class BulletSprite(Sprite):                             #玩家子弹精灵租
    def __init__(self,imagepath,pos,speed,direction):
        super().__init__()
        self.image = pygame.image.load(imagepath)
        # self.image = self.image.subsurface(rect)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = speed
        self.dir = direction
    def move(self):
        if self.dir == 0:
            self.rect.y -= self.speed
        elif self.dir > 0 :
            self.rect.y -= self.speed * math.sin(self.dir)
            self.rect.x -= self.speed * math.cos(self.dir+90)
        else:
            self.rect.y -= self.speed * math.sin(self.dir * -1 )
            self.rect.x += self.speed * math.cos(self.dir * -1 + 90)
        if self.rect.y < -50:
            self.kill()
    def update(self):
        self.move()

class EnemyBulletSprite(Sprite):                             #敌机子弹精灵组
    def __init__(self,imagepath,pos,speed,direction):
        super().__init__()
        self.image = pygame.image.load(imagepath)
        # self.image = self.image.subsurface(rect)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = speed
        self.dir = direction
    def move(self):
        self.rect.y -= self.speed
        if self.rect.y < -50:
            self.kill()
    def move2(self):
        self.rect.y -= self.speed
        self.rect.x -= self.speed/2
        if self.rect.y < -50:
            self.kill()
    def move3(self):
        self.rect.y -= self.speed
        self.rect.x += self.speed/2
        if self.rect.y < -50:
            self.kill()
    def update(self):       #子弹发射方向
        if self.dir == 0:
            self.move()
        elif self.dir == -1:
            self.move2()
        elif self.dir == 1:
            self.move3()

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
        self.hp = 10000
        self.timer = 0
        # self.canfire = False
        self.bullettype = 0
        self.bulletnum = 10
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
        self.timer += 1
        if self.timer > 50:
            self.timer = 0
            if self.bullettype == 0:
                bullet = BulletSprite("images/bullet/bullet1.png",  [self.rect.x + 45, self.rect.y - 20], 6,0)
                self.bulletgroup.add(bullet)
            elif self.bullettype == 1:
                bullet = BulletSprite("images/bullet/bullet1.png", [self.rect.x + 30, self.rect.y - 20], 6,0)
                bullet2 = BulletSprite("images/bullet/bullet1.png", [self.rect.x + 60, self.rect.y - 20], 6,0)
                self.bulletgroup.add(bullet)
                self.bulletgroup.add(bullet2)
            elif self.bullettype == 2:
                bullet = BulletSprite("images/bullet/bullet1.png", [self.rect.x + 30, self.rect.y - 20], 6,0)
                bullet2 = BulletSprite("images/bullet/bullet1.png", [self.rect.x + 60, self.rect.y - 20], 6,0)
                bullet3 = BulletSprite("images/bullet/bullet3r.png", [self.rect.x + 60, self.rect.y - 20], 6,15)
                bullet4 = BulletSprite("images/bullet/bullet3l.png", [self.rect.x + 28, self.rect.y - 20], 6,-15.076)
                bullet5 = BulletSprite("images/bullet/bullet4r.png", [self.rect.x + 60, self.rect.y - 20], 6,45.5)
                bullet6 = BulletSprite("images/bullet/bullet4l.png", [self.rect.x + 25, self.rect.y - 20], 6,-45.5)
                self.bulletgroup.add(bullet)
                self.bulletgroup.add(bullet2)
                self.bulletgroup.add(bullet3)
                self.bulletgroup.add(bullet4)
                self.bulletgroup.add(bullet5)
                self.bulletgroup.add(bullet6)
                self.bulletnum -= 1
                if self.bulletnum <= 0:
                    self.bullettype = 1
    def update(self):
        self.bulletgroup.update()
        self.bulletgroup.draw(self.screen)
        self.move()
        self.fire()

CREATE_ENEMY = locals.USEREVENT + 1
CREATE_BOSS = locals.USEREVENT + 2
CREATE_BULLET_HELP = locals.USEREVENT + 3

def main():
    pygame.init()
    pygame.display.set_caption("雷霆战机")
    screen = pygame.display.set_mode((512,768))
    bggroup = Group()
    bgsprite = BGSprite("images/bg/bg0.jpg")
    bggroup.add(bgsprite)
    playergroup = Group()
    playersprite = PlayerSprite("images/hero/hero_b_03.png",[0,0,122,105],[bgsprite.rect.w/2 - 61 ,600],5,screen)
    playergroup.add(playersprite)
    enemygroup = Group()
    bullethelpgroup = Group()
    bossgroup = Group()
    pygame.time.set_timer(CREATE_ENEMY,random.randint(500,1000))
    pygame.time.set_timer(CREATE_BOSS, random.randint(3000, 5000))
    pygame.time.set_timer(CREATE_BULLET_HELP,random.randint(3000,5000))
    font = pygame.font.Font(None,32)

    while True:
        bggroup.update()
        bggroup.draw(screen)

        playergroup.update()
        playergroup.draw(screen)

        enemygroup.update()
        enemygroup.draw(screen)

        bossgroup.update()
        bossgroup.draw(screen)

        bullethelpgroup.update()
        bullethelpgroup.draw(screen)

        screen.blit(font.render("Score:"+str(playersprite.score) , True,(255, 0, 0)),(20,20))
        screen.blit(font.render("HP:" + str(playersprite.hp), True, (255, 0, 0)), (20, 60))

        pygame.display.update()

        check1 = pygame.sprite.groupcollide(playersprite.bulletgroup,enemygroup,True,False)#碰撞检测 销毁子弹 销毁敌机
        if check1:
            enemy.hp -= 1
            if enemy.hp <= 0:
                list(check1.values())[0][0].bomb()
                playersprite.score += 100
        check11 = pygame.sprite.groupcollide(playersprite.bulletgroup, bossgroup, True, False)  # 碰撞检测 销毁子弹 销毁敌机
        if check11:
            boss.hp -= 1
            if boss.hp <= 0:
                list(check11.values())[0][0].bomb()
                playersprite.score += 500
        check2 = pygame.sprite.groupcollide(playergroup,enemygroup,False,True)
        if check2:
            list(check2.values())[0][0].bomb()
            playersprite.hp -= 1
        check22 = pygame.sprite.groupcollide(playergroup, bossgroup, False, True)
        if check22:
            list(check22.values())[0][0].bomb()
            playersprite.hp -= 1
        #print(enemygroup)
        for enemy in enemygroup:
            check3 = pygame.sprite.groupcollide(playergroup,enemy.bulletgroup,False,True)
            if check3:
                playersprite.hp -= 1
                #playersprite.bullettype = 0
        for boss in bossgroup:
            check33 = pygame.sprite.groupcollide(playergroup,boss.bulletgroup,False,True)
            if check33:
                playersprite.hp -= 1
                #playersprite.bullettype = 0
        if playersprite.hp <= 0:
            playersprite.kill()
        check4 = pygame.sprite.groupcollide(playergroup,bullethelpgroup,False,True)
        if check4:
            if playersprite.bullettype <= 1:
                playersprite.bullettype += 1
                playersprite.bulletnum = 10
            else:
                playersprite.bulletnum = 10
        playersprite.fire()
        for event in pygame.event.get():
            # if event.type == locals.KEYUP:
            #     if event.key == locals.K_SPACE:
            #         playersprite.fire()
            if event.type == locals.QUIT:
                pygame.quit()
                exit()
            if event.type == CREATE_ENEMY:
                enemy = EnemySprite("images/enemy/enemy2.png",[random.randint(0,410),-50],2,screen,random.randrange(-1,1,2),0,1)
                enemygroup.add(enemy)
            if event.type == CREATE_BOSS:
                boss = EnemySprite("images/enemy/boss.png",  [random.randint(0, 410), -50], 1,screen, 0,1,15)
                bossgroup.add(boss)
            if event.type == CREATE_BULLET_HELP:
                bullethelp = BulletHelp("images/hero/supply.png",[0,0,40,41],[random.randint(0,410),-50],2,screen,random.randrange(-1,1,2))
                bullethelpgroup.add(bullethelp)
        #playersprite.fire() #自动开火


if __name__ == '__main__':
    main()