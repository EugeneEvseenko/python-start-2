from pygame import *
'''Необходимые классы'''

#класс-родитель для спрайтов 
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (55, 55))
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if (keys[K_LEFT] or keys [K_a]) and self.rect.x > 5:
            self.rect.x -= self.speed
        if (keys[K_RIGHT] or keys[K_d]) and self.rect.x <win_width - 80:
            self.rect.x += self.speed
        if (keys[K_UP] or keys[K_w]) and self.rect.y > 5:
            self.rect.y -= self.speed
        if (keys[K_DOWN] or keys[K_s])and self.rect.y < win_height -80:
            self.rect.y += self.speed

#класс-наследник для спрайта-врага (перемещается сам)
class Enemy(GameSprite):
    side = "left"
    def update(self):
        if self.rect.x <= 470:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

#класс для спрайтов-препятствий
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
 
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
 
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
 
    def draw_wall(self):
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))

'''Описание игры'''

#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

w1 = Wall(154, 205, 50, 100, 20 , 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20 , 10, 380)
w4 = Wall(154, 205, 50, 200, 130, 10, 350)
w5 = Wall(154, 205, 50, 450, 130, 10, 360)
w6 = Wall(154, 205, 50, 300, 20, 10, 350)
w7 = Wall(154, 205, 50, 390, 120, 130, 10)

#Персонажи игры:
packman = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font_basic = font.Font(None, 70)
font_attempts = font.Font(None, 20)
win = font_basic.render('Ты выиграл! +1 попытка', True, (255, 215, 0))
lose = font_basic.render('Ты проиграл! -1 попытка', True, (180, 0, 0))
restart = font_basic.render('Нажми R для перезапуска', True, (180, 0, 0))
exit_text = font_basic.render('Нажми E для выхода', True, (180, 0, 0))
attempts = 2
attempts_text = font_attempts.render(f'Осталось {attempts} попыток', True, (255, 255, 255))

#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

def collide(is_win = True):
    global attempts, finish, attempts_text
    finish = True
    if is_win:
        attempts+=1
        window.blit(win, (50, 200))
        window.blit(restart, (40, 250))
    else:
        attempts-=1
        window.blit(lose, (50, 200))
        if attempts != 0:
            window.blit(restart, (40, 250))
        else:
            window.blit(exit_text, (80, 250))
    attempts_text = font_attempts.render(f'Осталось {attempts} попыток', True, (255, 255, 255))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0, 0))
        
        packman.update()
        monster.update()
        
        packman.reset()
        monster.reset()
        final.reset() 
        
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        
        #Ситуация "Проигрыш"
        if sprite.collide_rect(packman, monster) or sprite.collide_rect(packman, w1) or sprite.collide_rect(packman, w2) or sprite.collide_rect(packman, w2) or sprite.collide_rect(packman, w3) or sprite.collide_rect(packman, w4) or sprite.collide_rect(packman, w5) or sprite.collide_rect(packman, w6) or sprite.collide_rect(packman, w7):
            collide(False)
            kick.play()

        #Ситуация "Выигрыш"
        if sprite.collide_rect(packman, final):
            collide()
            money.play()
    else:
        if key.get_pressed()[K_r] and attempts > 0:
            packman = Player('hero.png', 5, win_height - 80, 4)
            finish = False
        if key.get_pressed()[K_e]:
            game = False
    window.blit(attempts_text, (5,5))
    display.update()
    clock.tick(FPS)