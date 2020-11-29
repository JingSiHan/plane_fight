import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)
print('英雄的原点：%d, %d' % (hero_rect.x, hero_rect.y))
print('英雄的尺寸：%d, %d' % (hero_rect.width, hero_rect.height))
print('%d, %d' % hero_rect.size)
print(type(hero_rect.size))

# TODO .h 和 .height应该是一样的？
print(hero_rect.h)
print(hero_rect.height)


# 四个参数的意义：Rect(left, top, width, height) -> Rect
