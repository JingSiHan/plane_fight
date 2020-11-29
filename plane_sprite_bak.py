import random
import pygame


# 碰到使用固定数字，应该设置为常量: 刷新的帧率，屏幕的大小
FRAME_PER_SEC = 60
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 创建敌机事件定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1



class GameSprite(pygame.sprite.Sprite):
    """游戏精灵类。"""

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向移动。
        self.rect.y += self.speed


class BackGround(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 1.调用父类方法实现精灵类的实现，image, rect, speed
        super().__init__('./images/background.png')
        # 2.判断是否是交替图像，如果是，需要设置初始位置。
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1.调用父类的方法实现
        super().update()
        # 2.判断是否移出屏幕，如果移出屏幕，把图像移动到屏幕上方。
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵类"""

    def __init__(self):
        # 1. 调用父类方法创建敌机精灵，同时指定图片
        super().__init__('./images/enemy1.png')
        # 2. 指定敌机的初始随机速度，1 - 3
        self.speed = random.randint(1, 3)

        # 3. 指定敌机的初始随机位置
        self.rect.bottom = 0
        # 水平位置
        max_width = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_width)

    def update(self):
        # 1. 调用父类方法使用垂直移动。
        super().update()

        # 2. 判断是否飞出屏幕。如果飞出屏幕需要从精灵组中删除。
        if self.rect.y >= SCREEN_RECT.height:
            print('飞出屏幕，需要从精灵组删除。。。')
            # kill方法将精灵从所有精灵组中移除，精灵会自动被销毁。从而调用__del__()方法
            self.kill()  # 调用__del__()方法

    def __del__(self):
        print('敌机挂了。坠毁坐标：%s' % self.rect)


class Hero(GameSprite):
    """英雄精灵类"""

    def __init__(self):
        # 1.调用父类方法，设置图片和速度
        super().__init__('./images/me1.png', speed=0)

        # 2. 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 3. 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 英雄飞机的左右移动。
        self.rect.x += self.speed

        # 英雄飞机的移动边界
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # print('发射子弹...')
        for i in range(0, 3):
            # 1. 创建子弹精灵
            bullet = Bullet()
            # 2. 设置精灵位置
            bullet.rect.bottom = self.rect.y - 20 * i
            bullet.rect.centerx = self.rect.centerx
            # 3. 将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵类"""

    def __init__(self):
        # 调用父类初始化方法，设置子弹图片和速度
        super().__init__('./images/bullet1.png', speed=-2)

    def update(self):
        # 调用父类方法，让子弹沿垂直方向飞行。
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print('子弹被销毁。。。')
