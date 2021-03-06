import pygame

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

clock = pygame.time.Clock()

# 飞机的初始位置
hero_rect = pygame.Rect(150, 500, 102, 126)

while True:
    clock.tick(60)
    # 移动飞机的位置
    hero_rect.y -= 2
    if hero_rect.y <= (-126):
        hero_rect.y = 700

    event_list = pygame.event.get()

    if len(event_list) > 0:
        print(event_list)

    # blit更新位置
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    # 使用update刷新屏幕
    pygame.display.update()

pygame.display.update()

pygame.quit()
