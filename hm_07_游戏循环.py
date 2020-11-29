import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load('./images/background.png')
screen.blit(bg, (0, 0))

# 绘制英雄图像
hero = pygame.image.load('./images/me1.png')
screen.blit(hero, (150, 500))

# 刷新屏幕呈现图像
pygame.display.update()

i = 0
clock = pygame.time.Clock()

while True:

    # 刷新率，n次每秒。
    clock.tick(60)
    print(i)
    i += 1
    pass

pygame.quit()
