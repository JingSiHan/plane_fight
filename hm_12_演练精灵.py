import pygame
from plane_sprite import *

pygame.init()
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load('./images/background.png')
screen.blit(bg, (0, 0))

# 绘制英雄图像
hero = pygame.image.load('./images/me1.png')
screen.blit(hero, (189, 700))

# 刷新屏幕呈现图像
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 英雄的初始位置
hero_rect = pygame.Rect(150, 500, 102, 126)

# 创建敌机的精灵
enemy = GameSprite('./images/enemy1.png')
enemy1 = GameSprite('./images/enemy2.png', speed=2)
# 创建敌机的精灵组。和创建精灵一样，都在初始化部分完成
enemy_group = pygame.sprite.Group(enemy, enemy1)

# 游戏循环，游戏正式开始
while True:
    clock.tick(60)
    # 1. 移动飞机的位置
    hero_rect.y -= 2
    if hero_rect.y <= (-126):
        hero_rect.y = 700

    # 2. 监听事件，退出游戏。
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('游戏退出')
            pygame.quit()
            exit()

    # 3. blit更新英雄的位置
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # update - 让组中所有精灵更新位置
    enemy_group.update()
    # draw - 在此screen上绘制所有的精灵
    enemy_group.draw(screen)

    # 4. 使用update刷新屏幕
    pygame.display.update()

pygame.display.update()

pygame.quit()
