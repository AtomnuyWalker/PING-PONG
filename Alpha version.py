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


win_width = 700
win_height = 500
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load("More.jpg"), (win_width, win_height))

player1 = Plaaer('player.png', 23, win_height - 500, 10)
ball = Ball("myachik.png",300, win_height - 300, 6)
player2 = Player('player.png', 655, win_height - 500, 10)


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

        player1.reset()
        player2.reset()
        ball.reset()
    

    display.update()
    clock.tick(FPS)