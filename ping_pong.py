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
run = True
finish = False
FPS = 60
clock = time.Clock()
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background,(0, 0))
    display.update()
    clock.tick(FPS)