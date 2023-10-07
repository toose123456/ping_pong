from pygame import *
win_width = 700
win_height = 500
window = display.set_mode(
    (win_width, win_height)
)
display.set_caption('ping_pong')
background = transform.scale(
    image.load('galaxy.jpg'),
    (win_width, win_height)
)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x, player_y, player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
run = True
finish = False
FPS = 60
clock = time.Clock()
boll = GameSprite('asteroid.png',250, 250, 10, 50 ,50)
racet1=Player('bullet.png', 0, 100, 10, 50, 170)
racet2=Player('bullet.png', 650, 100, 10, 50, 170)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background,(0, 0))
    boll.reset()
    racet1.update_l()
    racet2.update_r()
    racet1.reset()
    racet2.reset()
    display.update()
    clock.tick(FPS)
