import pygame

pygame.init()

# 根据文档介绍：set_mode(size=(0, 0), flags=0, depth=0, display=0) -> Surface,
# 参数是一个元组。
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load('./images/background.png')

screen.blit(bg, (0, 0))

pygame.display.update()

while True:
    pass

pygame.quit()
