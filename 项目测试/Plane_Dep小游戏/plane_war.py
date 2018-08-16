#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pygame, sys, random, time
from pygame.locals import *

# 设置窗口个常量
WINDOW_HEIGHT = 768
WINDOW_WIDTH = 512

enemy_list = []
score = 0
is_restart = False


##定义地图类；
class Map:
    def __init__(self, img_path, window):
        self.x = 0
        # 两张图片循环；
        self.bg_img1 = pygame.image.load(img_path)
        self.bg_img2 = pygame.image.load(img_path)
        # 两张不同图片的高；
        self.bg1_y = -WINDOW_HEIGHT
        self.bg2_y = 0
        self.window = window

    def map_move(self):
        # 当地图1的 y轴移动到0，则重置
        if self.bg1_y >= 0:
            self.bg1_y = -WINDOW_HEIGHT
        # 当地图2的 y轴移动到 窗口底部，则重置
        if self.bg2_y >= WINDOW_HEIGHT:
            self.bg2_y = 0

        # 每次循环都移动1个像素速度；
        self.bg1_y += 3
        self.bg2_y += 3

    def display(self):
        self.window.blit(self.bg_img1, (self.x, self.bg1_y))
        self.window.blit(self.bg_img2, (self.x, self.bg2_y))


class HeroBullet:
    """英雄子弹类"""

    def __init__(self, img_path, x, y, window):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.window = window

    def display(self):
        self.window.blit(self.img, (self.x, self.y))

    def move(self):
        """向上飞"""
        self.y -= 10

    def is_hit_enemy(self, enemy):
        if pygame.Rect.colliderect(
                pygame.Rect(self.x, self.y, 20, 31),
                pygame.Rect(enemy.x, enemy.y, 100, 68)
        ):  # 判断是否交叉
            return True
        else:
            return False


class EnemyPlane:
    def __init__(self, img_path, x, y, window):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.window = window
        self.is_hited = False
        self.anim_index = 0
        self.hit_sound = pygame.mixer.Sound("res/baozha.ogg")


    def enemy_move(self):
        self.y += 5
        if self.y >= WINDOW_HEIGHT:  # 敌机超出下边窗重置x,y
            self.x = random.randint(0, random.randint(0, WINDOW_WIDTH - 100))
            self.y = 0


    def plane_down_anim(self):  # 敌机击中动画；
        if self.anim_index >= 21:
            self.anim_index = 0
            self.img = pygame.image.load("res/img-plane_%d.png" % random.randint(1, 7))
            self.x = random.randint(0, WINDOW_WIDTH - 100)
            self.y = 0
            self.is_hited = False
            return
        elif self.anim_index == 0:
            self.hit_sound.play()
        self.img = pygame.image.load("res/bomb-%d.png" % (self.anim_index // 3 + 1))
        self.anim_index += 1


    def enemy_display(self):
        if self.is_hited:
            self.plane_down_anim()
        self.window.blit(self.img, (self.x, self.y))


class HeroPlane:
    def __init__(self, img_path, x, y, window):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.window = window
        self.bullets = []
        self.is_hited = False
        self.is_anim_down = False
        self.anim_index = 0

    def is_hit_enemy(self, enemy):
        if pygame.Rect.colliderect(
                pygame.Rect(self.x, self.y, 120, 78),
                pygame.Rect(enemy.x, enemy.y, 100, 68)
        ):  # 判断是否交叉
            return True
        else:
            return False

    def hero_down_anim(self):
        if self.anim_index >= 21:
            self.is_hited = False
            self.is_anim_down = True
            return

        self.img = pygame.image.load("res/bomb-%d.png" % (self.anim_index // 3 + 1))
        self.anim_index += 1

    # 英雄战机展示；
    def hero_display(self):
        for enemy in enemy_list:
            if self.is_hit_enemy(enemy):
                enemy.is_hited = True
                self.is_hited = True
                self.hero_down_anim()
                break
        self.window.blit(self.img, (self.x, self.y))

    # 英雄战机发射子弹控制
    def hero_display_bullets(self):
        # 贴子弹图
        deleted_bullets = []
        for bullet in self.bullets:
            if bullet.y >= -31:  # 没有出边界
                bullet.display()
                bullet.move()
            else:  # 飞出边界
                deleted_bullets.append(bullet)

            for enemy in enemy_list:
                if bullet.is_hit_enemy(enemy):  # 判断是否击中敌机
                    enemy.is_hited = True
                    deleted_bullets.append(bullet)
                    global score
                    score += 10
                    break

        for out_window_bullet in deleted_bullets:
            self.bullets.remove(out_window_bullet)

    # 英雄战机移动
    def hero_move_left(self):
        if self.x >= 0 and not self.is_hited:
            self.x -= 5

    def hero_move_right(self):
        if self.x <= WINDOW_WIDTH - 120 and not self.is_hited:
            self.x += 5

    def hero_move_up(self):
        if self.y >= 0 and not self.is_hited:
            self.y -= 5

    def hero_move_down(self):
        if self.y <= WINDOW_HEIGHT - 78 and not self.is_hited:
            self.y += 5

    # 英雄战机开火；
    def hero_fire(self):
        # 创建子弹对象  子弹x = 飞机x + 飞机宽度的一半 - 子弹宽度的一半
        bullet = HeroBullet("res/bullet_9.png", self.x + 60 - 10, self.y - 31, self.window)
        # 显示子弹(贴子弹图)
        bullet.display()
        self.bullets.append(bullet)


class Game:
    def __init__(self):
        # 初始化游戏程序；
        pygame.init()
        # 设置标题,图标；
        pygame.display.set_caption("英雄飞机大战 v2.0")
        game_ico = pygame.image.load('res/app.ico')
        pygame.display.set_icon(game_ico)
        ##游戏音乐循环播放；
        pygame.mixer.music.load('res/bg2.ogg')
        pygame.mixer.music.play(-1)
        ##游戏的结束音乐：
        self.gameover_sound = pygame.mixer.Sound('res/gameover.wav')

        # 创建窗口；
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        # 创建地图对象；
        self.game_map = Map('res/img_bg_level_%d.jpg' % random.randint(1, 5), self.window)

        # 创建英雄战机对象；
        self.hero_plane = HeroPlane("res/hero2.png", 240, 500, self.window)
        # 创建敌机对象；
        for i in range(3):
            enemy_plane = EnemyPlane("res/img-plane_%d.png" % random.randint(1, 7),
                                     random.randint(0, WINDOW_WIDTH - 100), random.randint(-300, -70), self.window)
            enemy_list.append(enemy_plane)
        self.enemy_list = enemy_list
        # 创建文字对象；
        self.score_font = pygame.font.Font("res/SIMHEI.TTF", 40)

    ##窗口方文字的显示；
    def draw_text(self, content, size, x, y):
        font_obj = pygame.font.Font('res/SIMHEI.TTF', size)
        text = font_obj.render(content, 1, (255, 255, 255))
        self.window.blit(text, (x, y))

    ##界面键盘的事件的捕捉；
    def wait_game_input(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                    pygame.quit()
                elif event.type == KEYDOWN:
                    # esc终止程序
                    if event.key == K_ESCAPE:
                        sys.exit()
                        pygame.quit()
                    # 返回键重启程序；
                    elif event.key == K_RETURN:
                        global is_restart, score
                        is_restart = True
                        score = 0
                        return

    def game_start(self):
        # 贴背景图；
        self.game_map.display()
        self.draw_text("英雄飞机大战", 40, WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 3)
        self.draw_text("按Enter开始游戏, Esc退出游戏", 28, WINDOW_WIDTH / 3 - 140, WINDOW_HEIGHT / 2)
        pygame.display.update()
        self.wait_game_input()

    def game_over(self):
        # 先停音乐；
        pygame.mixer.music.stop()
        # 再播放over的音乐；
        self.gameover_sound.play()
        # 贴背景图；
        self.game_map.display()
        self.draw_text("战机被击落,得分为 %d" % score, 28, WINDOW_WIDTH / 3 - 100, WINDOW_HEIGHT / 3)
        self.draw_text("按Enter重新开始, Esc退出游戏.", 28, WINDOW_WIDTH / 3 - 140, WINDOW_HEIGHT / 2)
        pygame.display.update()
        self.wait_game_input()
        self.gameover_sound.stop()

    def key_control(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.hero_plane.hero_fire()
        # 获取连续按下的情况；
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            self.hero_plane.hero_move_left()
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            self.hero_plane.hero_move_right()
        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            self.hero_plane.hero_move_up()
        if pressed_keys[pygame.K_x] or pressed_keys[pygame.K_DOWN]:
            self.hero_plane.hero_move_down()

    def display(self):
        # 贴图片；
        self.game_map.display()
        self.game_map.map_move()

        # 贴英雄飞机；
        self.hero_plane.hero_display()
        self.hero_plane.hero_display_bullets()

        # 贴敌机；
        for enemy in enemy_list:
            enemy.enemy_display()
            # 让敌机移动
            if not enemy.is_hited:
                enemy.enemy_move()

        # 贴得文字分；
        score_text = self.score_font.render("得分:%d" % score, 1, (255, 255, 255))
        self.window.blit(score_text, (10, 10))

        # 刷新界面；
        pygame.display.update()

    def run(self):
        if is_restart == False:
            self.game_start()
        while True:
            # 显示界面：
            self.display()
            # 优化点；
            if self.hero_plane.is_anim_down:
                self.hero_plane.is_anim_down = False
                global enemy_list
                enemy_list = []
                break
            # 键盘控制；
            self.key_control()
            # 程序休息；
            time.sleep(0.01)
        self.game_over()


def main():
    while True:
        game = Game()
        game.run()


if __name__ == "__main__":
    main()
