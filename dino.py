from pygame import*
from random import randint
class Game_sprite(sprite.Sprite):
    def __init__(self, img, w, h, x, y):
        super().__init__()
        self.image = transform.scale(img, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        screen.blit(self.image, self.rect)
        
class Dino(Game_sprite):
    def __init__(self):
        super().__init__(image.load('KIIITY.png'), 127, 182, 120, 350)
        self.isJump = False
        self.jumpCount = -21

    def update(self):
        if self.isJump:
            self.rect.y += self.jumpCount
            self.jumpCount += 1
            if self.jumpCount > 21:
                self.jumpCount = -21
                self.isJump = False

        super().update()

dino = Dino()

class Cactus(Game_sprite):
    def __init__(self):
        super().__init__(image.load('cactus.png'), 102, 121, 1000, 409)
        self.speed = randint(-12, -9)
    def update(self):
        self.rect.x +=self.speed
        if self.rect.x <= -150:
            self.rect.x = randint(950, 1200)
            self.speed = randint(-12, -9)
        super().update()
        

cactus = Cactus()








screen = display.set_mode((900,600))
display.set_caption('MyGame')


background = transform.scale(image.load('way_3.png'),(900,600))

button_play = transform.scale(image.load('playy.png'),(200,80))
button_quit = transform.scale(image.load('quit.png'),(200,80))

clock = time.Clock()
game = True
menu = True
finish = True


while game:
    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                x,y = mouse.get_pos()
                if menu:
                    if x >350 and x< 550 and y>200 and y<280:
                        menu = False
                        finish = False
                        
                        dino = Dino()
                        cactus = Cactus()

                    if x > 350 and x <550 and y>400 and y<480:
                        game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                dino.isJump = True


    screen.blit(background,(0,0))
    if menu:
        screen.blit(button_play,(350,200))
        screen.blit(button_quit,(350,400))
    elif not(finish):
        if dino.rect.colliderect(cactus.rect):
            finish = True
            menu = True
        #тут игровой процесс 
        dino.update()
        cactus.update()
        


    display.update()
