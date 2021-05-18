from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (20, 100))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class GameSprite2(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameSprite3(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (20, 1000))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class  Plaaer(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite2):
    direction = "left"
    def update(self):
        if sprite.collide_rect(player1, ball):
            self.direction = "right"
        if sprite.collide_rect(player2, ball):
            self.direction = "left"
        if self.rect.x <= 1:
            self.direction = "right"
        if self.rect.x >= 650:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

back = (244, 164, 96)
win_width = 700
win_height = 500
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

player1 = Plaaer('player.png', 80, win_height - 500, 10)
ball = Ball("myachik.png",300, win_height - 300, 6)
player2 = Player('player.png', 600, win_height - 500, 10)
vorota1 = GameSprite3("vorota.png", 0, win_height - 1000, 10)
vorota2 = GameSprite3("vorota.png", 680, win_height - 1000, 10)
font.init()
font = font.Font(None, 70)
win1 = font.render("PLAYER 1 WIN!", True, (255, 255, 255))
win2 = font.render("PLAYER 2 WIN!", True, (255, 255, 255))
speed_x = 3
speed_y = 3
shot = 0
goal1 = 0
goal2 = 0


game = True
finish = False
clock = time.Clock()
FPS = 60


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0, 0))
        player1.update()
        player2.update()
        ball.update()
        vorota1.update()
        vorota2.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(vorota2, ball):
            window.blit(win1, (175, 200))
            finish = True
        if sprite.collide_rect(vorota1, ball):
            window.blit(win2, (175, 200))
            finish = True

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player1, ball):
            speed_x *= -1
            speed_y *= 1
            #shot += 1
        if sprite.collide_rect(player2, ball):
            speed_x *= 1
            speed_y *= -1
            #shot += 1

        player1.reset()
        player2.reset()
        ball.reset()
        vorota1.reset()
        vorota2.reset()


    display.update()
    clock.tick(FPS)
